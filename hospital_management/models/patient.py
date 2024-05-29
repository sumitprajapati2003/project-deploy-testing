from odoo import models, fields, api
from odoo.exceptions import ValidationError

# class Patient(models.Model):
#     _name = "hm.patient"
#     _description = "Patient Details"
#     _inherit = ['mail.thread','mail.activity.mixin']
#     _rec_name = "patient_name"

    # patient_id = fields.Char(string="Patient ID")
    # patient_name = fields.Char(string="Patient Name")

    # @api.constrains('phone')
    # def validate_phone_number(self, value):
    #     if not value.isdigit():
    #         raise ValidationError("Phone number must only contain numeric characters.")
    #     if len(value)!= 10:
    #         raise ValidationError("Phone number must be 10 digits long.")
        
    # phone = fields.Char(string="Phone number", validate=validate_phone_number, regex="^[0-9]*$")
    # phone = fields.Char(string="Phone number", regex="^[0-9]*$")
    # email = fields.Char(string="Email")
    # medical_history = fields.Text(string="Medical History")
    # allergies = fields.Text(string="Allergies")
    # insurance_provider = fields.Char(string="Insurance Provider")
    # insurance_id = fields.Char(string="Insurance ID")
    # next_of_kin_name = fields.Char(string="Next of Kin Name")
    # next_of_kin_relationship = fields.Char(string="Next of Kin Relationship")
    # next_of_kin_phone_number = fields.Char(string="Next of Kin Phone Number")
    # marital_status = fields.Selection([('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], string="Marital Status")
    # occupation = fields.Char(string="Occupation")
    # patient_age = fields.Integer(string="Patient Age")
    # patient_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Patient Gender")
    # patient_address = fields.Text(string="Patient Address")
    # specialty_ids = fields.Many2many("dr.specialties", string = "Category")
    # disease_ids =  fields.Many2many("patient.disease",string="Disease",domain="[('specialty_id', 'in', specialty_ids)]")
    # assign_doctor_ids = fields.Many2many('hm.doctor', domain="[('specialties_id','in',specialty_ids)]")
    # admit_date = fields.Date()
    # discharge_date = fields.Date()
    # blood_group = fields.Selection([
    #     ('A+', 'A+'),
    #     ('A-', 'A-'),
    #     ('B+', 'B+'),
    #     ('B-', 'B-'),
    #     ('AB+', 'AB+'),
    #     ('AB-', 'AB-'),
    #     ('O+', 'O+'),
    #     ('O-', 'O-'),
    # ])

  
    # # @api.onchange("category_ids")
    # # def _onchange_category_ids(self):
    # #     self.disease_ids = self.env["patient.disease"].search([('specialty_id','in',self.category_ids.ids)])

    # @api.model_create_multi 
    # def create(self, vals_list):
    #     for res in vals_list:
    #         res['patient_id'] = self.env['ir.sequence'].next_by_code('hm.patient.code')
    #     return super(Patient, self).create(vals_list)
    

    # def test_write(self):
    #     # obj = self.env['patient.disease']
    #     obj = self.env['hm.doctor']
    #     print('----id---',self.specialty_ids)
    #     print('----ids---',self.specialty_ids.ids)
    #     # record = obj.search([('specialty_id','in',self.specialty_ids.ids)])

    #     record = obj.search([('specialties_id','in',self.specialty_ids)])
    #     print('---record----->',record.doctor_name)
