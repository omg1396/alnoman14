# -*- coding: utf-8 -*-
from odoo import models, fields, api


# class CompanyInherit(models.Model):
#     _inherit = 'res.company'
#     _description = 'CompanyInherit'
#
#     is_without_footer_header = fields.Boolean("Without Footer And Header")

class AccountMove(models.Model):
    _inherit = 'account.move'

    is_without_footer_header = fields.Boolean("Without Footer And Header")



class AccountPayment(models.Model):
    _inherit = 'account.payment'

    is_without_footer_header = fields.Boolean("Without Footer And Header")


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_without_footer_header = fields.Boolean("Without Footer And Header")


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_without_footer_header = fields.Boolean("Without Footer And Header")
