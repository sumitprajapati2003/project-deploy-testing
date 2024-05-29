from odoo import models, fields, api

class Doctor(models.Model):
    _name = "hm.doctor"
    _description = "Doctor Details"
    _rec_name = "doctor_name"   
    _inherit = ['mail.thread','mail.activity.mixin']

    photo = fields.Image(string="Photo")     
    doctor_name = fields.Char(string="Doctor Name")
    doctor_id = fields.Char(string="Doctor ID")
    doctor_email = fields.Char(string="Email")
    doctor_phone = fields.Char(string="Phone")
    doctor_address = fields.Char(string="Address")
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')], string = "Gender") 
    date_of_birth = fields.Date(string="Date of Birth")
    education = fields.Char(string="Education")
    qualification = fields.Char(string="Qualification")
    specialties_id = fields.Many2one('dr.specialties')
    consultation_fee = fields.Float(string="Consultation Fee")
    is_available = fields.Boolean(string="Is Available")
    availability_ids = fields.One2many('hm.doctor_availability', 'doctor_id', string="Availability")
    assigned_patient_ids = fields.Many2many('res.partner', domain="[('is_staff','=','false')]")


    @api.model_create_multi
    def create(self, vals_list):
        for res in vals_list:
            res['doctor_id'] = self.env['ir.sequence'].next_by_code('hm.doctor.code')
            res['doctor_name'] = "Dr. "+res['doctor_name']
        doctor = super(Doctor, self).create(vals_list)    
        self.create_doctor_user(doctor)
        return doctor

    def create_doctor_user(self, doctor):    
        User = self.env['res.users']
        doctor_group = self.env.ref('hospital_management.group_doctor')
        user_type = self.env.ref('base.group_user')
        print("-doctor_group----------->", doctor_group)
        print("-doctor_group----------->", user_type.id)

        department = self.env['hm.department'].search([('name', 'ilike', 'Doctor')], limit=1)
        print("-department----------->", department)

        doctor_user = User.create({
            'name':doctor.name,
            'login': doctor.email,
            'email': doctor.email,
            'groups_id': [(4, doctor_group.id),(4,user_type.id)] if doctor_group else [],
        })
        
        doctor_user.partner_id.write({
            'is_staff': True,
            'staff_role_id': department.id
        })
        print("---------->>>",doctor_user)
        # doctor_user.partner_id.is_doctor = True
        return doctor_user


  

    