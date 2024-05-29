from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BloodBank(models.Model):
    _name = "blood.bank"
    _description = "Blood bank"
    _rec_name = "blood_group"

    blood_group = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ])
    quantity = fields.Integer(string="Quantity")
    # date = fields.Date(string="Date")
    donor_line = fields.One2many("blood.donor", "donor_id")
    


class BloodRequest(models.Model):
    _name = "blood.request"
    _description = "Blood Request"
    _rec_name = "patient_id"

    blood_group = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ], string="Blood Group", required=True)
    quantity = fields.Integer(string="Quantity", required=True)
    patient_id = fields.Many2one('res.partner', string="Patient", domain="[('is_staff', '=', False),('is_doctor','=',False)]")
    additional_info = fields.Text(string="Additional Information")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('requested', 'Requested'),
        ('fulfilled', 'Fulfilled'),
        ('cancelled', 'Cancelled'),
    ], string="Status", default='draft')    

    
    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        patient = self.env['res.partner'].search([('id','=',self.patient_id.id)]) 
        self.blood_group = patient.blood_group

    @api.model_create_multi
    def create(self, vals_list):
        blood_requests = super(BloodRequest, self).create(vals_list)
        for blood_request in blood_requests:
            blood_group = blood_request.blood_group
            if not blood_group:
                raise ValidationError("Blood Group is required.")

            blood_bank_object = self.env['blood.bank'].search([('blood_group', '=', blood_group)], limit=1)
            if not blood_bank_object:
                raise ValidationError("No blood bank object found for the specified blood group.")

            if blood_bank_object.quantity < blood_request.quantity:
                raise ValidationError(f"The entered blood quantity exceeds the available quantity in the blood bank. In the hospital bank, blood has only {blood_bank_object.quantity} ml.")

            blood_bank_object.quantity -= blood_request.quantity
            blood_request.state = 'requested'
        return blood_requests

    def write(self, vals):
        old_values = {rec.id: {'blood_group': rec.blood_group, 'quantity': rec.quantity} for rec in self}
        print("old_values------------", old_values)
        res = super().write(vals)

        for rec in self:
            print("old_values----blood quantity--------", rec.quantity)
            
            old_data = old_values.get(rec.id, {})  
            old_blood_group = old_data.get('blood_group')
            old_quantity = old_data.get('quantity')
            
            if 'blood_group' in vals or 'quantity' in vals:
                rec.state = 'requested'
                if vals.get('blood_group'):
                    blood_bank_object = self.env['blood.bank'].search([('blood_group','=',vals.get('blood_group'))], limit=1)
                    if vals.get('quantity') and blood_bank_object:
                        if blood_bank_object.quantity >= vals['quantity']:
                            blood_bank_object.quantity -= vals['quantity']
                        else:
                            raise ValidationError("The entered blood quantity exceeds the available quantity.")
                elif 'quantity' in vals:
                    blood_bank_object = self.env['blood.bank'].search([('blood_group','=',rec.blood_group)], limit=1)
                    if blood_bank_object:
                        blood_bank_object.quantity -= (vals['quantity'] - old_quantity)
        return res
    

    # def write(self, vals):
    #     old_values = [{'blood_group': rec.blood_group, 'quantity': rec.quantity} for rec in self]
    #     print("old--valus-0000000000",old_values)

    #     res = super().write(vals)
    #     if 'blood_group' in vals or 'quantity' in vals:
    #         for rec in self:
    #             rec.state = 'requested'
    #             # print("=---------=-=-=",vals.get('blood_group'))
    #             # print("=---------=-=-=", vals.get('quantity'))
    #             if vals.get('blood_group'):
    #                 blood_bank_object = self.env['blood.bank'].search([('blood_group','=',vals.get('blood_group'))], limit=1)
    #                 if vals.get('quantity') and blood_bank_object:

    #                     # print(">>>>>>>-------Second If statement------------->>>>..")
    #                     if blood_bank_object.quantity >= vals['quantity']:
    #                         blood_bank_object.quantity -= vals['quantity']
    #                     else:
    #                         raise ValidationError("The entered blood quantity exceeds the available quantity.")
    #             elif 'quantity' in vals:
    #                 for rec in self:
    #                     old_blood_quantity = self.env['blood.request'].search([('blood_group','=',rec.blood_group)], limit=1)
    #                     blood_bank_object = self.env['blood.bank'].search([('blood_group','=',rec.blood_group)], limit=1)
    #                     print("--old_blood_quantity-------", old_blood_quantity.quantity)
    #                     print("--blood_bank_object-------", blood_bank_object.quantity)
    #                     print("--vals['quantity']-------",vals['quantity'])
    #                     print("--rec']-------",rec.quantity)
    #                     blood_bank_object.quantity -= (vals['quantity']-old_blood_quantity.quantity)
    #                     print("--blood_bank_object----after---", blood_bank_object.quantity)
                       
    #     return res


    def action_draft(self):
        self['state']  = 'draft'
    
    def action_requested(self):
        self['state']  = 'requested'

    
    def action_fulfilled(self):
        template = self.env.ref('hospital_management.blood_request_fullfilled_mail_id')
        for rec in self:
            print('---rec id---',rec.patient_id)
            template.send_mail(rec.patient_id.id, force_send=True) 
            rec.state  = 'fulfilled'

    def action_cancelled(self):
        self['state']  = 'cancelled'
