from odoo import fields, models, _,api


class CarEnquireWizard(models.TransientModel):
    _name = 'car.enquire.wizard'
    _description='car enquire wizard'

    partner_id=fields.Many2one('res.partner',string="partner_id")
    states=fields.Selection(selection=[('sell','Sell'),('buy','Buy')])
    fleet_id=fields.Many2one('fleet.vehicle.model',string="Car Model" )
    category=fields.Many2one(related="fleet_id.category_id",string="category",readonly=False)
    fuel_type=fields.Selection(related="fleet_id.default_fuel_type",string="Fuel Type",readonly=False)
    color=fields.Char(string="Color")
    model_year=fields.Char(string="Model Year")
    number_of_seats=fields.Integer(string="Seat Number")

    @api.model        
    def default_get(self,fields):
        res=super(CarEnquireWizard,self).default_get(fields)
    #     print(self.env.context,"-----------------context")
        change_user=self.env['car.enquire'].sudo().browse(self.env.context.get('active_ids'))
        print(change_user.partner_id.id,'user<<<<<<<<<<,')
        res['partner_id']=change_user.partner_id.id
        res['fleet_id']=change_user.fleet_id.id
        res['category']=change_user.category.id
        res['fuel_type']=change_user.fuel_type
        res['model_year']=change_user.fuel_type
        res['number_of_seats']=change_user.number_of_seats
        res['states']=change_user.states
        print('default get ---')
   
        return res
    def confirm(self):
        print('sudo check-------')
        print(self.env.context,'Context <<<<<<<<<<<<<<<<')
        print(self.env.context['active_id'],'><><><><><<<<<<<<<<<<. active ids')
        change_user=self.env['car.enquire'].sudo().browse(self.env.context.get('active_ids'))
        print(change_user.ids,'change users')

        search_car=self.env['sell.buy'].sudo().search([('fleet_id','=',change_user.fleet_id.id)])
        print(search_car,'search_car------------')
        print(change_user.states,'-state--',change_user.data_true,'data true')
        for rec in search_car:
            if rec.states=="sell":
                print(rec,'sell.buy  record delete -------')
                rec.sudo().unlink()

        if change_user.data_true and change_user.states=="sell":
            print(change_user.states,'states----------')
            print(self,'self wizard============================')
            self.env["sell.buy"].sudo().create({
                'partner_id':change_user.partner_id.id,
                'model_year':change_user.model_year,
                'fleet_id':change_user.fleet_id.id,
                'category':change_user.category.id,
                'states':change_user.states,
                'car_image':change_user.car_image,
                'color':change_user.color,
                'customer_price':change_user.customer_price,
            })
            change_user.sudo().unlink()
        else:
            self.env["sell.buy"].sudo().create({
                'partner_id':change_user.partner_id.id,
                'model_year':change_user.model_year,
                'fleet_id':change_user.fleet_id.id,
                'category':change_user.category.id,
                'states':'purchased_by_customer',
                'car_image':change_user.car_image,
                'customer_price':change_user.customer_price,
                'color':change_user.color
            })
            change_user.sudo().unlink()
            # search_car_seller.unlink()
            print('else run car purchased_by_customer')

        print('Create_sell/by Record......................')   