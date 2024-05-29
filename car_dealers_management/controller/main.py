from odoo import http, _
from odoo.http import request
from datetime import datetime
import base64

class SellBuyController(http.Controller):
    @http.route('/enquire', type='http', auth='public', website=True)
    def sell_buy_enquire(self, **post):
        public_user = request.env.user.has_group('base.group_public')
        current_user=request.env.user.partner_id
        # print(current_user,'current user enquire=====================')
        fleet_id=request.env['fleet.vehicle.model'].sudo().search([])
        print(post),'post<<<<<<<<<<<<<<<<<<<<<<<,,'
        return request.render('car_dealers_management.car_enquire',{'partner_id':current_user,'fleet_id':fleet_id,'public_user':public_user})
    
    @http.route('/enquire-data', type='http', auth='public', website=True)
    def sell_buy_enquire_car(self, **post):
        print(post,'post<<<<<<<<<<<<<<<<<<<<<<<,,')
        images=post.get('car_image')
        print(images,'images.....................')
        post.update({
            'car_image':base64.b64encode(images.read()) or False
        })
        print(post['data_true'],'data ------------check')
        request.env['car.enquire'].create(post)
        return request.render('car_dealers_management.enquire_successful')
    
    @http.route('/car-buy', type='http', auth='public', website=True)
    def sell_car(self, **post):
        sell_cars=request.env['sell.buy'].sudo().search([('states','=','sell')])
        return request.render('car_dealers_management.sell_cars',{'sell_cars':sell_cars})
    
    @http.route('/car-detail/<int:car_id>', type='http', auth='public', website=True)
    def sell_car_detail(self, car_id=None, **post):
    
        sell_cars=request.env['sell.buy'].sudo().search([('id','=',int(car_id))])
        public_user = request.env.user.has_group('base.group_public')
       
        print(sell_cars,'sell car details ------------------ sell')
        return request.render('car_dealers_management.car_detail',{'sell_cars':sell_cars, 'public_user': public_user})

    @http.route('/buy-successfully/<int:buyer_id>', type='http', auth='public', website=True)
    def sell_car_successfully(self, buyer_id=None, **post):
        # print(request.env.user.name,'buy partner --------------')
        browse_data=request.env['sell.buy'].sudo().browse(buyer_id)
        print(browse_data.states,'browse data-------------')
        print(post,'buy Post-------------------------buyer',browse_data.states)
        
        request.env['car.enquire'].sudo().create({
            'partner_id':request.env.user.partner_id.id,
            'fleet_id':browse_data.fleet_id.id,
            'category':browse_data.category.id,
            'model_year':browse_data.model_year,
            'states':'buy',
            'customer_price':post.get("customer_price")
        })
        return request.render('car_dealers_management.car_successfully_buys')
    
    @http.route('/car-track', type='http', auth='public', website=True)
    
    def car_track(self,  **post):
        current_user=request.env.user.partner_id.id
        public_user = request.env.user.has_group('base.group_public')
        search_user=request.env["sell.buy"].sudo().search([('partner_id','=',current_user)])
        search_enquire=request.env["car.enquire"].sudo().search([('partner_id','=',current_user)])

        return request.render('car_dealers_management.tracking_template',{'search_user':search_user,'search_enquire':search_enquire,'public_user':public_user})

    
    






















    
    # @http.route('/registration', type='http', auth='public', website=True,csrf=False)
    # def office_registration_submit(self, **post):
    #     file = post.get('office_doc')
    #     attachment_list = request.httprequest.files.getlist('office_doc')
    #     print(attachment_list,'<<<---------attachment_list')
    #     value={
    #         'name':post.get('name'),
    #         'office_email':post.get('office_email'),
    #         'office_doc':base64.b64encode(file.read()) or False,
    #         'filename': file.filename,
    #         'partner_id':request.env.user.partner_id.id,
    #         'start_time':datetime.now()
    #     }
       
    #     office_id=request.env['office.info'].sudo().create(value)

    #     for att in attachment_list:
    #         attachments = {
    #             'res_name': att.filename,
    #             'res_model': 'office.info',
    #             'res_id': office_id.id,
    #             'datas': value['office_doc'],
    #             'type': 'binary',
    #             'name': att.filename,
    #         }
    #         print(attachments,'attachments>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>........')
    #         store=request.env['ir.attachment'].sudo().create(attachments)
    #         print(store,'<<<<<<<<<<<store\n\n')
    #     # return request.redirect('/office')
    #     return request.render('building_managaments.registration_successful')

    # @http.route('/office', type='http', auth='public', website=True)
    # def office_data(self, **post):
    #     # return 'hello world'
    #     print('user>>',request.env.user.id)
    #     search_rec=request.env['office.info'].sudo().search([('partner_id','=',request.env.user.partner_id.id)])

    #     return request.render('building_managaments.office_website',{'search_rec':search_rec})
    
    # @http.route(['/office-info/<int:office_id>','/office-info/<model("office.info"):office>']
    #             ,type='http', auth='public', website=True)
    # def office_info(self,office_id=None,office=None,**post):
    #     rec=request.env['office.info'].search([('id','=',int(office_id))])
    #     print('controller>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.....',rec)
    #     return request.render('building_managaments.office_web',{'office_id':rec})

