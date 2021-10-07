# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class website_elnoman(models.Model):
#     _name = 'website_elnoman.website_elnoman'
#     _description = 'website_elnoman.website_elnoman'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
