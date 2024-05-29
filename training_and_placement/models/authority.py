from odoo import models, fields

class Authority(models.Model):
    _name = 'authority.authority'
    _description = 'Authority'

    # _inherit = 'res.partner'

    # company_id = fields.Many2one('company.company', string='Company') 
    # authority_channel_ids = fields.Many2many('mail.channel', string='Channels')

    name = fields.Char(string='Name')
    image = fields.Image(string='Image')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    position = fields.Char(string='Position')