from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    print_stamp = fields.Boolean(string='Print Stamp')
