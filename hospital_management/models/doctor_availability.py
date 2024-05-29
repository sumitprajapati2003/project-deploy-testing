from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Day(models.Model):
    _name = 'hm.day'
    _description = "Doctor availability days"

    name = fields.Char(string="Day", required=True)
    # name = fields.Selection([
    #     ('monday', 'Monday'),
    #     ('tuesday', 'Tuesday'),
    #     ('wednesday', 'Wednesday'),
    #     ('thursday', 'Thursday'),
    #     ('friday', 'Friday'),
    #     ('saturday', 'Saturday'),
    #     ('sunday', 'Sunday')
    # ], string="Day", required=True)

class DoctorAvailability(models.Model):
    _name = 'hm.doctor_availability'
    _description = "Doctor availability"
    _rec_name = "doctor_id"

    doctor_id = fields.Many2one('res.partner', string="Doctor", domain="[('is_staff', '=', False)]", required=True)
    day_ids = fields.Many2many('hm.day', string="Day", required=True)
    start_time = fields.Float(string="Start Time", required=True)
    end_time = fields.Float(string="End Time", required=True)
    # start_time = fields.Datetime(string="Start Time", required=True, widget='time')
    # end_time = fields.Datetime(string="End Time", required=True, widget='time')
    # start_time = fields.Float(string="Start Time", required=True, widget='web_widget_timepicker')
    # end_time = fields.Float(string="End Time", required=True, widget='web_widget_timepicker')


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            existing_availability = self.search([('doctor_id', '=', vals.get('doctor_id'))])
            if existing_availability:
                raise ValidationError("Doctor availability already exists for this doctor.")
        return super(DoctorAvailability, self).create(vals_list)

    @api.constrains('start_time', 'end_time')
    def _check_time_format(self):
        time_list = []
        for record in self:
            try:
                for record in self:
                    if record.start_time >= record.end_time:
                        raise ValidationError('Start Time should be less than End Time')
                    if not(0 <= record.start_time <= 24) or not(0 <= record.end_time <= 24):
                        raise ValidationError('Invalid time format. Time should be between 00:00 and 24:00')

                # start_time_dict = self._validate_time(str(record.start_time))
                # end_time_dict = self._validate_time(str(record.end_time))
                # time_list.append({'start_hour': start_time_dict['hours'], 'start_minutes': start_time_dict['minutes'],
                #                 'end_hour': end_time_dict['hours'], 'end_minutes': end_time_dict['minutes']})
                # print("Time List:", time_list)
                # for time in time_list:
                #     # if time['start_hour'] > time['end_hour'] and time['start_minutes'] <=60 and time['end_minutes'] <=60:
                #     if time['start_hour'] > time['end_hour'] or (time['start_hour'] == time['end_hour'] and time['start_minutes'] > time['end_minutes']):
                #         raise ValidationError('Start Time should be less than End Time')
                    
            except ValidationError as e:
                raise ValidationError(e)

    # def _validate_time(self, time_str):
    #     try:

    #         hours, minutes = time_str.split('.')
    #         hours = int(hours)
    #         minutes = int(minutes)
    #         if not(0 <= hours <= 24) or not(0 <= minutes <= 60):
    #             raise ValidationError("Invalid time format. Please use HH:MM format.")
    #         return {'hours': hours, 'minutes': minutes}
    #     except ValueError:
    #         raise ValidationError("Invalid time format. Please use HH:MM format.")