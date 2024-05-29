from odoo import fields,models


class Amenities(models.Model):
    _name='hotel.amenities'
    _description='Amenities Room'
    _rec_name='room_type'


    room_type=fields.Selection([('king_size','King Size'),('super_deluxe','Super Deluxe'),('deluxe','Deluxe')])
    person=fields.Integer(string='Maximum Allowed Person')
    amenities_group_ids=fields.Many2many('hotel.amenities.group',string='Amenities')
    room_price=fields.Integer(string='Room Price')
    hotel_room_id=fields.Many2one('hotel.room')
    


