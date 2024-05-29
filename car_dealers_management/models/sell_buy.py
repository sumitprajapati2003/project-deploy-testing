from odoo import fields,models,api
import base64
class CarCar(models.Model): 
    _name="sell.buy"
    _inherit=['mail.thread', 'mail.activity.mixin']

    partner_id=fields.Many2one('res.partner',string="sellers/buyer")
    states=fields.Selection(selection=[('purchased_by_customer','Purchased by customer'),('sell','Sell'),('buy','Buy')], default="purchased_by_customer")
    fleet_id=fields.Many2one('fleet.vehicle.model',string="Car Model" )
    category=fields.Many2one(related="fleet_id.category_id",string="category",readonly=False)
    fuel_type=fields.Selection(related="fleet_id.default_fuel_type",string="Fuel Type",readonly=False)
    color=fields.Char(string="Color")
    model_year=fields.Char(string="Model Year")
    car_image=fields.Image(string="Car Images")
    number_of_seats=fields.Integer(string="Seat Number")
    brand_id=fields.Many2one("fleet.vehicle.model.brand",string="Seat Number")
    # car_logo=fields.Binary(related="brand_id.image_128",string="Seat Number")
    car=fields.Binary(string="car logo")
    car_price=fields.Integer(string="Car Price")
    customer_email=fields.Char(string="Email")
    customer_price=fields.Integer(string="Customer Price")

    def in_sell(self):
        for rec in self:
            rec.states="sell"
    def in_buy(self):
        for rec in self:
            rec.states="buy"
    print('change by mehul-----')        


    def mail_send(self):
        if self.states=="purchased_by_customer":
            print(self.states,'send mail-----------')
        
            mail_template=self.env.ref('car_dealers_management.mail_template_sell_buy')
            compose_form = self.env.ref('mail.email_compose_message_wizard_form')
            ctx = {
                'default_model': 'sell.buy',
                'default_res_ids': self.ids,
                'default_template_id': mail_template.id,
                'default_composition_mode': 'comment',
                'mark_so_as_sent': True,
                'default_email_layout_xmlid': 'mail.mail_notification_layout_with_responsible_signature',
                'proforma': self.env.context.get('proforma', False),
                'force_email': True,
                # 'model_description': self.with_context(lang=lang).type_name,
            }
            return {
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'mail.compose.message',
                'views': [(compose_form.id, 'form')],
                'view_id': compose_form.id,
                'target': 'new',
                'context': ctx,
            }         