from odoo import models, fields

class Course(models.Model):
    _name = 'course.course'
    _description = 'Training Course'

    name = fields.Char(string='Name', required=True)
    image = fields.Image(string='Image')
    description = fields.Text(string='Description',translate=True)
    duration = fields.Integer(string='Duration (in hours)')
    fees = fields.Integer(string='Fees')
    trainee_ids = fields.One2many('trainee.trainee', 'course_id', string='Trainee')
    placed_ids = fields.One2many('placement.placement', 'course_id', string='placed')
    trainer_id = fields.One2many('res.partner',string="Trainer",inverse_name='course_id')
    
    
    