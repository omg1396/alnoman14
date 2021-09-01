# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def force_cancel(self):
        for rec in self:
            rec.sudo().write({'state': 'cancel'})
