from odoo import models, fields ,api
from odoo.exceptions import ValidationError




class Applications(models.Model):
    _name = 'applications.applications'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'applications'
    _rec_name = "student_id"
        
    applications_id = fields.Char(readonly=True)
    student_id = fields.Many2one('trainee.trainee',string="Student")
    email = fields.Char(string="Email" , compute = "_trainee_email")
    company_id = fields.Many2one('company.company', string='Company ')
    position_id = fields.Many2one("company.career",string='Position')
    
    
    state = fields.Selection(selection=[
       ('pending', 'Pending'),
       ('selected', 'Selected'),
       ('rejected', 'Rejected'),
    ], tracking=True,string='Status', required=True, copy=False,
    default='pending')
    
    # sequence 
    @api.model_create_multi
    def create(self, vals):
        for rec in vals:
            rec['applications_id'] = self.env['ir.sequence'].next_by_code('applications.applications')
        res = super().create(vals)
        return res
    
    # if student is selected the student cannot apply again 
    @api.model_create_multi
    def create(self, vals):
        for rec in vals:
            rec['applications_id'] = self.env['ir.sequence'].next_by_code('applications.applications')
        
        student_ids = [val['student_id'] for val in vals]
        previous_applications = self.env['applications.applications'].search([('student_id', 'in', student_ids), ('state', '=', 'selected')])
        
        if previous_applications:
            raise ValidationError("A student is Selected in previous Application")
        
        res = super().create(vals)
        return res
    
    def action_open_multi_step_wizard(self):
        self.ensure_one()
        action = self.env.ref('training_and_placement.action_multi_step_wizard').read()[0]
        action['context'] = {
            'default_student_id': self.student_id.id,
            'default_company_id': self.company_id.id,
            'default_position_id': self.position_id.id,
        }
        return action
                
    def _trainee_email(self):
        self.email = " "
        if self.student_id:
            self.email = self.student_id.email

    
                    
    def action_rejected(self):
        for rec in self:
            rec.state = "rejected"
            
    def action_selected(self):
        for rec in self:
            rec.state = "selected"