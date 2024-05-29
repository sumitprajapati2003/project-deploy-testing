from odoo import fields,models,api

class CarEnquire(models.Model): 
    _name="car.enquire"

    
    partner_id=fields.Many2one('res.partner',string="sellers/buyer")
    states=fields.Selection(selection=[('sell','Sell'),('buy','Buy'),('reject','Reject'),])
    fleet_id=fields.Many2one('fleet.vehicle.model',string="Car Model" )
    category=fields.Many2one(related="fleet_id.category_id",string="category",readonly=False)
    fuel_type=fields.Selection(related="fleet_id.default_fuel_type",string="Fuel Type",readonly=False)
    color=fields.Char(string="Color")
    model_year=fields.Char(string="Model Year")
    car_image=fields.Image(string="Car Images")
    car_price=fields.Integer(string="Car Price")
    data_true=fields.Boolean(string="Data")
    customer_price=fields.Integer(string="Customer Price")
    number_of_seats=fields.Integer(string="Seat Number")

    def in_sell(self):
        for rec in self:
            rec.states="sell"
            print('--------------rec---------------')
            print('--------------rec---------------')

    def in_buy(self):
        for rec in self:
            rec.states="buy"
    def in_confirm(self):
        for rec in self:
            rec.states="confirm"
    def confirm_order(self):
        return {
            'type': 'ir.actions.act_window',
            'name': ('enquire wizard'),
            'view_mode': 'form',
            'res_model': 'car.enquire.wizard',
            'target': 'new',
            'views': [[self.env.ref('car_dealers_management.car_enquire_form_view').id, 'form']]
        }   
    def cancel_order(self):
        print('before cancel_order------------------',self.states) 
        self.states="reject"
        print('after cancel_order------------------',self.states) 

    def fun(self):
        pass    
     