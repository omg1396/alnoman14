from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    print_stamp = fields.Boolean('Print Stamp?')
