from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    latest_product = fields.Boolean("Latest Product")
