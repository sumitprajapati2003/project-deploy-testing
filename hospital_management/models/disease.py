from odoo import models, fields

class Disease(models.Model):
    _name = "patient.disease"
    _description = "Patient Disease"
    _rec_name = "disease_name"
    _inherit = ['mail.thread','mail.activity.mixin']

    disease_name = fields.Char(string="Disease", required=True)
    # patient_ids = fields.Many2many("hm.patient",string="Patients")
    specialty_id = fields.Many2one("dr.specialties", string = "Category")

    