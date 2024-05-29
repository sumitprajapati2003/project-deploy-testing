from odoo import models , fields , api
from odoo.exceptions import ValidationError

class PlacementWizard(models.TransientModel):
    _name = "placement.wizard"
    _description = "placement wizard"
    
    
    
    company_id = fields.Many2one('company.company', string='Company')
    student_id = fields.Many2one('trainee.trainee', string='Student')
    course_id = fields.Many2one('course.course', string='Course')
    job_title = fields.Many2one("company.career",string='Job Title')
    salary = fields.Integer(string='Salary')
    
    
    def create_placement(self):
        placement = self.env['placement.placement'].create({
            'student_id': self.student_id.id,
            'company_id': self.company_id.id,
            'course_id': self.course_id.id,
            'job_title': self.job_title.id,
            'salary': self.salary,
        })
