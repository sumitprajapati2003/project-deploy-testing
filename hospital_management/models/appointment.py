from odoo import models, fields,api
from datetime import datetime,timedelta
from odoo.exceptions import ValidationError


class Appointment(models.Model):
    _name = 'appointment.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'appointment_time desc'
    _rec_name = "patient_id"

    patient_id = fields.Many2one('res.partner', domain="[('is_staff', '=', False),('is_doctor','=',False)]")
    doctor_id = fields.Many2one('res.partner', domain="[('is_doctor','=',True)]")
    booking_date = fields.Date(string="Booking Date")
    day_ids = fields.Many2many('hm.day', string="Day")
    doctor_availability = fields.Char(string="Availability Time") #This field store doctor's start time and end time 
    # appointment_time = fields.Datetime(string="Appointment Time")
    appointment_time = fields.Float(string="Appointment Time", required=True)

    @api.onchange('patient_id','booking_date')
    def _onchange_patient_id(self):
        if self.patient_id:
            primary_doctor = self.patient_id.primary_doctor_id

            if primary_doctor:
                self.doctor_id = primary_doctor.id
                selected_day = self.booking_date.strftime('%A') if self.booking_date else ""

                if selected_day and selected_day not in primary_doctor.availability_ids.day_ids.mapped('name'):
                    raise ValidationError(f'On {selected_day}, {primary_doctor.name} is not available.')

                self.day_ids = primary_doctor.availability_ids.day_ids
                self.doctor_availability = f"{primary_doctor.availability_ids.start_time} to {primary_doctor.availability_ids.end_time}"



    # @api.onchange('patient_id','booking_date')
    # def _onchange_patient_id(self):
    #     # if self.patient_id:
    #     #     doctor_ids = self.patient_id.assign_doctor_ids.ids
    #     #     print("-->>>>>>>>>>",doctor_ids)
    #     #     self.doctor_id = [(6, 0, doctor_ids)]  # Using the "command" (6, 0, ids) to set Many2many field
    #     print("self--->-----------", self)
    #     if self.patient_id:
    #         primary_doctor = self.patient_id.primary_doctor_id

    #         if primary_doctor:
    #             self.doctor_id = primary_doctor.id
    #             # selected_day = datetime.strptime(self.booking_date, '%Y-%m-%d').strftime('%A')
    #             selected_day = ""

    #             if self.booking_date:
    #                 selected_day = self.booking_date.strftime('%A')
    #             self.day_ids =  primary_doctor.availability_ids.day_ids

    #             for day in primary_doctor.availability_ids.day_ids:
    #                 print("primary_doctor----day",day.name) 
    #                 print("selected_day----day",selected_day) 
    #                 if day.name != selected_day and selected_day :
    #                     raise ValidationError(f'On {selected_day}, {primary_doctor.doctor_name} is not available. ')
    #                 self.booking_date = self.booking_date

    #             self.doctor_availability = f"{primary_doctor.availability_ids.start_time} to {primary_doctor.availability_ids.end_time}" 
    #             # print("self.booking_date-----------------",self.booking_date)
    #             # print("primary_doctor----day",primary_doctor.availability_ids.day_ids)  
    #             # print("primary_doctor----start_time",primary_doctor.availability_ids.start_time)  
    #             # print("primary_doctor----end_time----------",primary_doctor.availability_ids.end_time)  
    

    @api.constrains('booking_date', 'appointment_time')
    def _check_booking_date(self):
        for record in self:
            if record.booking_date and record.booking_date < fields.Date.today():
                raise ValidationError("Booking date cannot be in the past.")
           
            if record.appointment_time:
                if not record.doctor_id:
                    raise ValidationError("Please select a doctor.")
                
                start_time = record.doctor_id.availability_ids.start_time
                end_time = record.doctor_id.availability_ids.end_time
                
                if record.appointment_time < start_time or record.appointment_time > end_time:
                    raise ValidationError(f"Appointment time should be between {start_time} and {end_time}.")
                
                existing_appointments = self.search([
                    ('doctor_id', '=', record.doctor_id.id),
                    ('appointment_time', '=', record.appointment_time),
                    ('booking_date', '=', record.booking_date),
                    ('id', '!=', record.id)  # Exclude the current appointment
                ])

                if existing_appointments:
                    raise ValidationError("Appointment already exists for the same doctor at the same time.")

    def appointment_mail_reminder(self):
        today = fields.Date.today()
        print("today-----------",today)
        tomorrow = today + timedelta(days=1)
        print("tomorrow--->",tomorrow)
        appointments_day_before = self.search([('booking_date','>=',tomorrow)])
        '''
        booking_date : 30 May
        today = 29 May
        tomorrow = 30 May
        appointments_day_before = self.search([('booking_date','>=',tomorrow)])
        '''


        print("appointments_day_before->>>>>>>>-------",appointments_day_before)
        for appointment in appointments_day_before:
            template = self.env.ref('hospital_management.appointment_reminder_mail_id')
            template.send_mail(appointment.id, force_send=True)


