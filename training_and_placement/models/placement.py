from odoo import models, fields ,api

class Placement(models.Model):
    _name = 'placement.placement'
    _description = 'Placement'
    _rec_name = "student_id"

    company_id = fields.Many2one('company.company', string='Company')
    student_id = fields.Many2one('trainee.trainee', string='Student')
    course_id = fields.Many2one('course.course', string='Course')
    job_title = fields.Many2one("company.career",string='Job Title')
    salary = fields.Integer(string='Salary')
