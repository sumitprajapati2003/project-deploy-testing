from odoo import http
from odoo.http import request
import base64

class CourseDetail(http.Controller):
    
    @http.route('/course', type='http', auth='public',website=True)
    def course_data(self, **post):
        course_data = request.env["course.course"].search([ ])
        values = {
                    "records": course_data
                    } 

        return request.render("training_and_placement.course_template",values)
        
        
    @http.route('/course/<int:course_id>', type='http', auth='public',website=True)
    def course_detail(self,course_id=None,**post):
        course = request.env["course.course"].search([("id","=",course_id)])
        print("course_iddddddddddddddddd__________________________",course.name)
        values = {
                    "course_id": course
                    }
        
            
        if not course:
            return request.redirect('/course')
        else:
            return request.render("training_and_placement.course_detail_template",values)
    
    
    
    @http.route('/course/register', type='http', auth='public',website=True, csrf=False)
    def register(self):
        courses = request.env['course.course'].search([])

        return request.render("training_and_placement.register_template",{'courses': courses})

    
    @http.route('/course/register/thankyou', type='http', auth='public',website=True)
    def submit(self , **post):
        print("-------post------------\n\n\n\n\n\n",post)
        
        user = request.env.user
        
        values={
            "name":post["name"],
            "email":post["email"],
            "phone":post["phone"],
            "resume":base64.encodebytes(post.get('file').read()) or False,
            "store_fname":post["name"] + "_document",
            # "course_id":post["courses"]
        }
        
        record = request.env[('trainee.trainee')].sudo().create(values)
        print('----------record-----',record)
        
        name = record.name + "_attachment"
        attachment = request.env['ir.attachment'].sudo().create({
        'name': name,
        'type': 'binary',
        'datas':values["resume"],
        'store_fname': name,
        'res_model': "trainee.trainee",
        'res_id': record.id,
        'mimetype': 'application/x-pdf'
        })
        
        return request.render("training_and_placement.thankyou_template",values)    