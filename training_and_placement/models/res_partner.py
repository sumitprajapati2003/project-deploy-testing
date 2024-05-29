from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    course_id = fields.Many2one('course.course', string='Course')
    resume = fields.Binary(string='Resume')
    store_fname = fields.Char(string="File Name")
    