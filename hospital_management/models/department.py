from odoo import models, fields

class Department(models.Model):
    _name = "hm.department"
    _description = "Department Details"

    name = fields.Char(string="Name", required=True)
