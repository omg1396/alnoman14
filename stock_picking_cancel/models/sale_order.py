from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def force_cancel(self):
        for rec in self:
            rec.picking_ids.force_cancel()
            rec.sudo().write({'state': 'cancel'})