from odoo import fields,models


class HotelRoomBooking(models.Model):
    _name='hotel.room.booking'
    _description='Hotel Room'
    _rec_name='hotel_room_id'


    hotel_room_id=fields.Many2one(string='name')
    room_type_id=fields.Many2one('hotel.amenities',string='Room Type')
    room_status=fields.Char()
    
