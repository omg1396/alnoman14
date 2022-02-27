from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    print_stamp = fields.Boolean('Print Stamp?')
