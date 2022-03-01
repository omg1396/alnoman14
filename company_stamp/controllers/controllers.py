# -*- coding: utf-8 -*-
# from odoo import http


# class CompanyStamp(http.Controller):
#     @http.route('/company_stamp/company_stamp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/company_stamp/company_stamp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('company_stamp.listing', {
#             'root': '/company_stamp/company_stamp',
#             'objects': http.request.env['company_stamp.company_stamp'].search([]),
#         })

#     @http.route('/company_stamp/company_stamp/objects/<model("company_stamp.company_stamp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('company_stamp.object', {
#             'object': obj
#         })
