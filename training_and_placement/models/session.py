from odoo import models, fields
import datetime

class Session(models.Model):
    _name = 'session.session'
    _description = 'Training Session'
    _rec_name = "course_id"

    course_id = fields.Many2one('course.course', string='Course')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    started = fields.Boolean(string='Course Started')
    trainer = fields.Many2one("res.partner",string='Trainer')
    today = fields.Date(string='Today', default=datetime.date.today())
    
    def fun(self):
        print("kjfhsjhdfjshdfhjdsj0----------------d")
        
    def check_session_start_date(self):
        print("_________________/////////////////____________________session start date")
        session_ids = self.search([])
        for rec in session_ids:
            if rec.start_date < rec.today:
                rec.started = True
            else:
                rec.started = False