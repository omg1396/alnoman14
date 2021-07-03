from odoo import fields, models, api


class ResCurrency(models.Model):
    _inherit = 'res.currency'



    def write(self, vals):


        if 'rounding' in vals:
            rounding_val = vals['rounding']
            for record in self:
                if (rounding_val > record.rounding or rounding_val == 0) and record._has_accounting_entries():
                    continue
        return