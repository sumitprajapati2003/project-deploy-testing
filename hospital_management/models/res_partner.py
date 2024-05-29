from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _rec_name = "name"

    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
    marital_status = fields.Selection([('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], string="Marital Status")

    # Doctor related field
    doctor_id = fields.Char(string="Doctor ID", compute="_compute_id")
    is_doctor = fields.Boolean(string = "Is Doctor")
    education = fields.Char(string="Education")
    qualification = fields.Char(string="Qualification")
    specialties_id = fields.Many2one('dr.specialties')
    consultation_fee = fields.Float(string="Consultation Fee")
    is_available = fields.Boolean(string="Is Available")
    availability_ids = fields.One2many('hm.doctor_availability', 'doctor_id', string="Availability")
    # assigned_patient_ids = fields.Many2many('res.partner', domain="[('is_staff','=',False)]")
    assigned_patient_ids = fields.Many2many(
        comodel_name='res.partner',
        relation='assigned_patients_rel',
        column1='partner_id',
        column2='patient_id',
        string='Assigned Patients',
        domain="[('is_staff','=',False)]",
    )


    # Patient related field
    medical_history = fields.Text(string="Medical History")
    allergies = fields.Text(string="Allergies")
    insurance_provider = fields.Char(string="Insurance Provider")
    insurance_id = fields.Char(string="Insurance ID")
    occupation = fields.Char(string="Occupation")
    specialty_ids = fields.Many2many("dr.specialties", string = "Disease Category")
    disease_ids =  fields.Many2many("patient.disease",string="Disease",domain="[('specialty_id', 'in', specialty_ids)]")
    # assign_doctor_ids = fields.Many2many('res.partner', domain="[('specialties_id','in',specialty_ids),('is_available', '=', True)]")
    assign_doctor_ids = fields.Many2many(
        comodel_name='res.partner',
        relation='res_assigned_doctors_rel',
        column1='partner_id',
        column2='doctor_id',
        string='Assigned Doctors',
        domain="[('specialties_id','in',specialty_ids),('is_doctor','=',True),('is_available','=',True)]",
    )

    primary_doctor_id = fields.Many2one('res.partner', string="Primary Doctor", domain="[('specialties_id','in',specialty_ids),('is_available', '=', True)]")
    admit_date = fields.Date(default=fields.Date.today())
    discharge_date = fields.Date(default=False)
    blood_group = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ])

    is_staff = fields.Boolean(string = "Is Staff")
    staff_role_id = fields.Many2one("hm.department", string="Department")
    staff_name = fields.Char(related="staff_role_id.name")

    
    @api.depends("doctor_id")
    def _compute_id(self):
        for res in self:
            res['doctor_id'] = self.env['ir.sequence'].next_by_code('hm.doctor.code')
            res['doctor_name'] = "Dr. "+res['doctor_name']
        # doctor = super(ResPartner, self).create(vals_list)    
        # self.create_doctor_user(doctor)

    @api.model_create_multi
    def create(self, vals_list):
        doctor = super(ResPartner, self).create(vals_list)    

        print("doctor-------->",doctor.is_doctor)
        if doctor.is_doctor:
            self.create_doctor_user(doctor)

        return doctor
    
    def create_doctor_user(self, doctor):    
        User = self.env['res.users']
        doctor_group = self.env.ref('hospital_management.group_doctor')
        user_type = self.env.ref('base.group_user')
        print("-doctor_group----------->", doctor_group)
        print("-doctor_group----------->", user_type.id)

        department = self.env['hm.department'].search([('name', 'ilike', 'Doctor')], limit=1)

        doctor_user = User.create({
            'name':doctor.doctor_name,
            'login': doctor.doctor_email,
            'email': doctor.doctor_email,
            'groups_id': [(4, doctor_group.id),(4,user_type.id)] if doctor_group else [],
        })

        return doctor_user

    # @api.model_create_multi 
    # def create(self, vals_list):
    #     for res in vals_list:
    #         print('-res----->>>>',res)
           # res['patient_id'] = self.env['ir.sequence'].next_by_code('hm.patient.code')
        # return super(ResPartner, self).create(vals_list)

    # @api.constrains('discharge_date')
    # def _check_discharge_date(self):
    #     print('-------',self.discharge_date)
    #     if self.is_staff:
    #         self.admit_date = False
    #         self.discharge_date = False
            
    #     if self.discharge_date:
    #         for rec in self:
    #             if rec.discharge_date < rec.admit_date:
    #                 raise ValidationError("The Discharge date cannot be set in the past")

    @api.constrains('admit_date', 'discharge_date')
    def _check_discharge_date(self):
        for record in self:
            if record.discharge_date and record.admit_date and record.discharge_date < record.admit_date:
                raise ValidationError("The Discharge date cannot be set in the past")                
                    

    # def action_send_email_with_temp(self):
    #     template = self.env.ref('hospital_management.blood_request_fullfilled_mail_id')
    #     print("-----template--------", template)
    #     for rec in self:
    #         template.send_mail(rec.id) 

    # def appointment_mail_reminder(self):
    #     template = self.env.ref('hospital_management.appointment_reminder_mail_id')
    #     print("-----------------------------------------------------------------",self)
    #     for rec in self:
    #         print('---rec id---',rec.patient_id)
    #         template.send_mail(rec.patient_id.id, force_send=True) 
    #         rec.state  = 'fulfilled'
