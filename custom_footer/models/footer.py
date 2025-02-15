# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CompanyInherit(models.Model):
    _inherit = 'res.company'
    _description = 'CompanyInherit'

    is_without_footer_header = fields.Boolean("Reports Without Footer And Header")

class BaseDocumentLayout(models.TransientModel):
    _inherit = 'base.document.layout'

    is_without_footer_header = fields.Boolean(related='company_id.is_without_footer_header')