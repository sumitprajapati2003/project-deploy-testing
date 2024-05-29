from odoo import fields,models


class HotelHistory(models.Model):
    _name='room.history'
    _description='Room History'


    from_book_date=fields.Date(string='Form Booked Date')
    to_book_date=fields.Date(string='to Booked Date')
    person_name=fields.Many2one('res.partner',string='Person Name')
    mobile=fields.Char(string='Mobile')
    rooms=fields.Char(string='Rooms')
    state=fields.Char(string='State')
    # room_type_name=fields.Selection(string='Room Type')
    room_type_names=fields.Char(string='Room Type')
    room_price=fields.Integer(string='One Day Room Price')
    total_price=fields.Integer(string='Total Room Price')

    

