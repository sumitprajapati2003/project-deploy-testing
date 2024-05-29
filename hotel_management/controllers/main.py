from odoo import http
from odoo.http import request
import base64


class StudentDetail(http.Controller):

    @http.route('/rooms', auth='public', type='http', website=True)
    def rooms_data(self, **post):
        records=request.env['hotel.room'].sudo().search([])
        print(records,',..,.,.,.,.Records,.,.,.,.,.,.,.,.,.,.')
        return request.render("hotel_management.hotel_room_template",{'records':records})
   
    @http.route(['/room-detail','/room-detail/<int:room_id>'], auth='public', type='http', website=True)
    def room_detail(self,room_id=None,**post):
        records=request.env['hotel.room'].sudo().search([('id','=',int(room_id))])
    #     print(records,',..,.,.,.,.,.,.,.,.,.,.,.,.,.,.')
        return request.render("hotel_management.rooms_detail_template",{'records':records})
    
    @http.route(['/book-room','/book-room/<int:book>'],auth='public', type='http', website=True)
    def book_room(self,book=None,**post):
        records=request.env['hotel.room'].sudo().search([('id','=',book)])
        print(records,',..,.,.,.,.,.,.,.,.,.,.,.,.,.,.')
        return request.render("hotel_management.room_booking_template",{'records':records})
    


    # @http.route(['/room-detail','/room-detail/<model("student.detail"):student>','/student-detail/<int:student_id>'], auth='public', type='http', website=True)
    # def student_detail_data(self, student=None,student_id=None,**post):
    #     records=request.env['student.detail'].sudo().search([('id','=',int(student))])
    #     print(records,',..,.,.,.,.,.,.,.,.,.,.,.,.,.,.')
    #     return request.render("school_management.student_detail_template",{'records':records})
    

    # @http.route('/register', auth='public', type='http', website=True)
    # def register_form(self,**post):
    #     websites=request.env['website'].sudo().search([])
    #     print('websites <><><>><><><><><',websites)

    #     return request.render("school_management.student_register",{
    #         'websites':websites
    #     })
    


    # def register_forms(self,**post):
    #     # del post['website']
    #     # print(post,' post <><><><><>><><<><><><><><><>')
    #     # post.pop('website')                                   
    #     file = post.get('document')
    #     file_list = request.httprequest.files.getlist('document')
    #     # print('file',file)
    #     value={
    #         'name':post.get('name')+'ddd',
    #         'student_mail':post.get('student_mail'),
    #         'phone':post.get('phone'),
    #         'document':base64.b64encode(file.read()) or False,
    #         'filename':file.filename,
    #         'parent_id':request.env.user.partner_id.id,

    #     }
    #     # print(value,'value <><><><><>><><<><><><><><><>')
    #     record=request.env['student.detail'].sudo().create(value)
    #     for fil in file_list:
    #         # print('fil><><><><><><><><><><',fil)
    #         create1= {
    #                     'res_name':fil.filename,
    #                     'res_model':"student.detail",
    #                     'name':fil.filename,
    #                     'type': 'binary',
    #                     # 'datas': base64.b64encode(fil.read()), 
    #                     'datas': value['document'],
    #                     'res_id': record.id,
    #                         }
    #         # print(create1, '----------------create1\n\n')
    #         attachment = request.env['ir.attachment'].sudo().create(create1)
    #     # print(record.id,'<><><><><><><><><><><><><><><><><><><><><><><><><', attachment)
    #     print(',..,.,.,.,.,.,.,.,.,.,.,.,.,.,.')
    #     return request.render("website.contactus_thanks")
    

    
    #     # return request.redirect('/contactus-thank-you') 
    














        
#         return request.render("training_and_placement.thankyou_template",values)    
# has context menu

#         print(file,'file  <><><><><><><><><><>><><')
#         if file:
#             # Process the file, for example, save it as attachment
#                 'name': file.filename,
#                 'mimetype':'application/pdf',
#                 'type':'file',
#                 'datas': base64.encodestring(file.read()),
#                 'datas_fname': file.filename,
#                 'res_model': 'student.detail',  # specify the model you want to attach to
#                 'res_id': create_record.id  # specify the record id to which you want to attach
#             })
    
