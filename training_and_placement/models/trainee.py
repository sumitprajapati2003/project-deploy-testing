from odoo import models, fields

class Trainee(models.Model):
    _name = 'trainee.trainee'
    _description = 'Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    image = fields.Image(string='Image')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    course_id = fields.Many2one('course.course', string='Course')
    resume = fields.Binary(string='Resume')
    store_fname = fields.Char(string="File Name")
    
    