from odoo import fields,models


class AmenitiesGroup(models.Model):
    _name='hotel.amenities.group'
    _description='Amenities Room'


    

    name=fields.Char(string='Name')
    # amenities_id=fields.Many2one('hotel.amenities')
