# models.py
from odoo import models, fields


class CustomPurchase(models.Model):
    _name = 'custom.purchase'
    _description = 'Custom Purchase'

    company_name = fields.Char(string='Company Name')

    company_type = fields.Selection([
        ('person', 'Individual'),
        ('company', 'Company')
    ], string="Company Type", required=True, default='person')
    company_name = fields.Char("Company Name")
    country_code = fields.Char("Country Code")
    street = fields.Char("Street")
    # street2 = fields.Char("Street2")
    city = fields.Char("City")
    state_id = fields.Many2one('res.country.state', string="State")
    zip = fields.Char("ZIP")
    country_id = fields.Many2one('res.country', string="Country")
    vat = fields.Char("Tax ID")

    mobile = fields.Char("Mobile")
    email = fields.Char("Email", required=False)
    website = fields.Char("Website")

    customer = fields.Boolean(help="Double Validation Amount")
    vendor = fields.Boolean(help="Double Validation Amount")
