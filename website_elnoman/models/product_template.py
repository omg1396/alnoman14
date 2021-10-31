from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    latest_product = fields.Boolean("Latest Product")
    product_properties_ids = fields.One2many('product.properties','product_id',"Product Properties")

class ProductProperties(models.Model):
    _name = 'product.properties'
    _description = "Product Properties"

    product_id = fields.Many2one('product.template')
    name = fields.Char("Description")
