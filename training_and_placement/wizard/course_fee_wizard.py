from odoo import models , fields , api

class CourseFeeWizard(models.TransientModel):
    _name = "course.fee.wizard"
    _description = "course fee wizard"
    
    fees = fields.Float(string='Fee')
                            
    def change_fee(self):
        print("self......................",self)
        fees_id = self.env['course.course'].browse(self._context['active_ids'])
        for course_fee in fees_id:
            course_fee['fees'] = self.fees
    
