# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteElnoman(http.Controller):
#     @http.route('/website_elnoman/website_elnoman/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_elnoman/website_elnoman/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_elnoman.listing', {
#             'root': '/website_elnoman/website_elnoman',
#             'objects': http.request.env['website_elnoman.website_elnoman'].search([]),
#         })

#     @http.route('/website_elnoman/website_elnoman/objects/<model("website_elnoman.website_elnoman"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_elnoman.object', {
#             'object': obj
#         })
