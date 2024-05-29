from odoo import models, fields, api

class MultiStepWizard(models.TransientModel):
    _name = 'multi.step.wizard'
    _description = 'Multi Step Wizard'

    step1 = fields.Char(string='Step 1')
    step2 = fields.Char(string='Step 2')
    step3 = fields.Char(string='Step 3')

    def action_next_step(self):
        if self.step1:
            self.step2 = 'Step 2 completed'
        if self.step2:
            self.step3 = 'Step 3 completed'
        return self.write({'step1': False, 'step2': False, 'step3': False})

    def action_previous_step(self):
        if self.step3:
            self.step2 = False
        if self.step2:
            self.step1 = False
        return self.write({'step1': False, 'step2': False, 'step3': False})