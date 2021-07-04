# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CompanyInherit(models.Model):
    _inherit = 'res.company'
    _description = 'CompanyInherit'

    is_without_footer_header = fields.Boolean("Without Footer And Header")

