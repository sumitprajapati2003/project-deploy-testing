from odoo import fields,models


class HotelRoom(models.Model):
    _name='hotel.room'
    _description='Hotel Room'


    name=fields.Char(string='name')
    room_price=fields.Integer(string='Room Price')
    room_type_id=fields.Many2one('hotel.amenities',string='Room Type')
    
#     amenities_line=fields.One2many('hotel.amenities',"hotel_room_id",string='Room Type')

    state=fields.Selection(selection=[('draft','Draft'),('check_in','CheckIn'), 
    ('check_out','Check_Out')],copy=False,default='draft', string='State',store=True)
    customer_name=fields.Many2one('res.partner',string='customer_name',readonly=True)
    mobile=fields.Char(string='Mobile',readonly=True)
    room_book_date=fields.Date(string='Book Room Date',readonly=True)
    room_out_date=fields.Date(string='Room Out Date',readonly=True)
#     total_price=fields.Integer(string='Total Price')
    

    


    def book_room(self):
        value ={
                'name': ('Book Room'),
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'target': 'new',
                'res_model':'room.book',
                'views': [[self.env.ref('hotel_management.room_book_wizard_form').id,'form']]
        }
        return value
    
    def book_room_out(self):
            
            
        value ={
                        'name': ('Room Out'),
                        'type': 'ir.actions.act_window',
                        'view_mode': 'form',
                        'target': 'new',
                        'res_model':'room.book',
                        'views': [[self.env.ref('hotel_management.room_book_wizard_form').id,'form']]
                }
        return value

        

