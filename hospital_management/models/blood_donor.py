from odoo import models, fields,api


class Donor(models.Model):
    _name = "blood.donor"
    _description = "Blood donor"
    _rec_name = "name"

    name = fields.Char(string="Donor Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
    blood_group = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ],  string="Blood Group")
    medical_history = fields.Text(string="Medical History")
    quantity = fields.Integer(string="Quantity")
    # blood_bank_line = fields.One2many('blood.bank','donor_id', string="Blood Bank")    
    donor_id = fields.Many2one('blood.bank', string="Donor")
    date = fields.Date(string="Date", default=fields.Date.today())



    @api.model_create_multi
    def create(self, vals):
        donor = super(Donor, self).create(vals)
        blood_bank = self.env['blood.bank'].search([('blood_group', '=', donor.blood_group)], limit=1)
        if blood_bank:
            blood_bank.write({'quantity': blood_bank.quantity + donor.quantity})
        else:
            blood_bank = self.env['blood.bank'].create({
                'blood_group': donor.blood_group,
                'quantity': donor.quantity,
            })

        # blood_bank = self.env['blood.bank'].create({
        #     'blood_group':donor.blood_group,
        #     'quantity':donor.quantity,
        #     'donor_line':[(4,donor.id,False)]
        # })
        donor.write({'donor_id': blood_bank.id})
        return donor
    

    # def write(self, vals):
    #     donor = super().write(vals)
    #     updated_donor = self.env['blood.donor'].browse(self.id)
    #     print("-donor__write------>",updated_donor.blood_group)
    #     return donor


        