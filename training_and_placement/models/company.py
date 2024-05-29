from odoo import models, fields ,api

class Company(models.Model):
    _name = 'company.company'
    _description = 'Company'


    # company_authority_id = fields.Many2one('authority.authority', string='Company Authority')

    name = fields.Char(string='Name', required=True)
    title = fields.Char(compute="compute_title",readonly=True)
    detail = fields.Text(string='Detail')
    phone = fields.Char(string='phone')
    email = fields.Char(string='Email')
    image = fields.Image(string='Image')
    address = fields.Text(string='Address')
    contact_person = fields.Char(string='Contact')
    website = fields.Char(string='Website')
    career_ids = fields.One2many('company.career', 'company_id', string='Career')
    

    
    
    def compute_title(self):
        for record in self:
            record.title = record.name + ' ' + 'Company'
            


class Career(models.Model):
    _name = 'company.career'
    _description = 'Career'
    _rec_name = "position"
    
    
    company_id = fields.Many2one('company.company', string='Company')
    vacancy = fields.Integer(string='Vacancy')
    position = fields.Char(string='Position')
    skill = fields.Char(string="Req. Skill")
    job_detail = fields.Char(string='Job Detail')
    