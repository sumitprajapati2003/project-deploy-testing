from odoo import fields, models,api,_
from odoo.exceptions import ValidationError
import datetime



class Room_Book_Wizard(models.TransientModel):
    _name = 'room.book'
    _description = 'Room Book'
    _inherit =['mail.thread','mail.activity.mixin']


    from_book_date=fields.Date(default=fields.Date.today(),string='Form Booked Date')
    to_book_date=fields.Date(string='to Booked Date',required=True)
    person_name=fields.Many2one('res.partner',string='Person Name',required=True)
    mobile=fields.Char(string='Mobile',required=True)
    rooms_id=fields.Char(string='Rooms',readonly=True)
    room_in=fields.Boolean(string='Room In')
    room_type=fields.Many2one('hotel.amenities',string='Room Type')
    price=fields.Integer(string='One Day Price',readonly=True)
    state=fields.Char()
    total_price=fields.Integer(string='Total Price')
    customer_email=fields.Char(string='Email')


    # @api.constrains("mobile")   
    # def phone_number(self):
    #     if self.mobile:
    #         if len(self.mobile) !=10:
    #             raise ValidationError(_("Mobile Number Is Not Valid "))
    #         else:
    #                 if self.mobile.isalpha():
    #                     raise ValidationError(_("Enter Your Valid Mobile Number"))
  
    @api.model
    def default_get(self, fields_list):
        print(fields_list,"<><><><><><>><><><><><",self)
        defaults = super(Room_Book_Wizard,self).default_get(fields_list)
        room = self.env['hotel.room'].browse(self.env.context.get('active_ids'))
        print(room.room_type_id.room_price,"-----------ROOM---------------")

        defaults['rooms_id']=room.name
        defaults['price']=room.room_type_id.room_price
        defaults['room_type']=room.room_type_id.id
        defaults['person_name']=room.customer_name.id
        defaults['mobile']=room.mobile
        defaults['from_book_date']=room.room_book_date
        defaults['to_book_date']=room.room_out_date

        return defaults
    

   


    def book_room_action(self):
        
        print(self.room_type,'-----------------------------')
        room = self.env['hotel.room'].browse(self.env.context.get('active_ids'))
        print('-------------------',room.room_type_id.room_type)
        
        if self.env.context['room_status'] == 'check_in':
            room.customer_name=self.person_name.id 
            room.mobile=self.mobile
            room.room_book_date=self.from_book_date
            room.room_out_date=self.to_book_date
            room.state = 'check_in'
            self.state='check_in'
            self.room_in=False

            store=self.env['room.history'].create({
                'from_book_date':self.from_book_date,
                'to_book_date':self.to_book_date,
                'person_name':self.person_name.id,
                'mobile':self.mobile,
                'rooms':self.rooms_id,
                'state':self.state,
                'room_type_names':room.room_type_id.room_type,
                'room_price':room.room_type_id.room_price,
                'total_price':self.total_price  
            })
        
            template = self.env.ref('hotel_management.mail_template_room_book')
            compose_form = self.env.ref('mail.email_compose_message_wizard_form')

            ctx = {
                'default_model': 'room.book',
                'default_res_ids': self.ids,
                'default_template_id':template.id,
                'default_composition_mode':'comment',
                'mark_so_as_sent': True,
                'default_email_layout_xmlid': 'mail.mail_notification_layout_with_responsible_signature',
                'proforma': self.env.context.get('proforma', False),
                'force_email': True,
            }
            return {
                'type': 'ir.actions.act_window',
                'view_mode':'form',
                'res_model':'mail.compose.message',
                'views': [(compose_form.id,'form')],
                'view_id': compose_form.id,
                'target': 'new',
                'context': ctx,
            }
                
        if self.env.context['room_status'] == 'check_out':
                    self.state='check_out'
                    store=self.env['room.history'].create({
                        'from_book_date':self.from_book_date,
                        'to_book_date':self.to_book_date,
                        'person_name':self.person_name.id,
                        'mobile':self.mobile,
                        'rooms':self.rooms_id,
                        'state':self.state,
                        'room_type_names':room.room_type_id.room_type,
                        'room_price':room.room_type_id.room_price,
                        'total_price':self.total_price
                    })
                    room.customer_name=False
                    room.mobile=False
                    room.room_book_date=False
                    room.room_out_date=False

                    room.state = 'draft'
                    return self.env.ref('hotel_management.hotel_room_detail_report').report_action(store)  
   
   
    @api.onchange("from_book_date","to_book_date")
    def _onchange_total(self):
        if self.from_book_date == self.to_book_date:
                self.total_price=self.price

        elif self.from_book_date and self.to_book_date:
                days=self.to_book_date - self.from_book_date
                print(days.days,'---------days---------')
                self.total_price=(days.days)*self.price


                    



        # print('self<><>><-----------------------------',self.env.context)
        # print(room.state)
    

   

       


