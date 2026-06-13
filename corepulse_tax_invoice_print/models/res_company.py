# -*- coding: utf-8 -*-
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    invoice_header_image = fields.Binary(
        string='Invoice Header Image',
        attachment=True,
        help='Displayed full-width at the top of every invoice PDF page.',
    )
    invoice_footer_image = fields.Binary(
        string='Invoice Footer Image',
        attachment=True,
        help='Displayed full-width at the bottom of every invoice PDF page.',
    )
