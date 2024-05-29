from odoo import models , fields , api
from odoo.exceptions import ValidationError



class SessionReportWizard(models.TransientModel):
    _name = "session.report.wizard"
    _description = "session report wizard"
    
    session_list_ids = fields.Many2many("session.session",string="Sessions")
    from_date = fields.Date(string="From Date")
    to_date = fields.Date(string="To Date")

    def create_report(self):
        sessions = self.env['session.session'].search([
            ('start_date', '>=', self.from_date),
            ('start_date', '<=', self.to_date),
        ])
        if len(sessions)>0:
            print("oooooooooooo___________________",sessions.ids)
            print("oooooooooooo___________________",self)
            return self.env.ref("training_and_placement.action_report_session").report_action(sessions)
        else:
            raise ValidationError("No sessions found within the specified date range.")
            # return {
            #     'type': 'ir.actions.act_window',
            #     'name': ('session wizard'),
            #     'view_mode': 'form',
            #     'res_model': 'session.report.wizard',
            #     'target': 'new',
            #     'views': [[self.env.ref('training_and_placement.view_session_report_wizard_form').id, 'form']],
            #     }
 