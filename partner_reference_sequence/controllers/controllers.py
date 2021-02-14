# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerReferenceSequence(http.Controller):
#     @http.route('/partner_reference_sequence/partner_reference_sequence/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_reference_sequence/partner_reference_sequence/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_reference_sequence.listing', {
#             'root': '/partner_reference_sequence/partner_reference_sequence',
#             'objects': http.request.env['partner_reference_sequence.partner_reference_sequence'].search([]),
#         })

#     @http.route('/partner_reference_sequence/partner_reference_sequence/objects/<model("partner_reference_sequence.partner_reference_sequence"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_reference_sequence.object', {
#             'object': obj
#         })
