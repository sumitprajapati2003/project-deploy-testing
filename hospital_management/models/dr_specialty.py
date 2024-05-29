from odoo import models, fields

class Specialties(models.Model):
    _name = "dr.specialties"
    _description = "Doctor Specialties"
    
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    