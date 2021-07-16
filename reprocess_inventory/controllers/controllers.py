# -*- coding: utf-8 -*-
# from odoo import http


# class ReprocessInventory(http.Controller):
#     @http.route('/reprocess_inventory/reprocess_inventory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reprocess_inventory/reprocess_inventory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reprocess_inventory.listing', {
#             'root': '/reprocess_inventory/reprocess_inventory',
#             'objects': http.request.env['reprocess_inventory.reprocess_inventory'].search([]),
#         })

#     @http.route('/reprocess_inventory/reprocess_inventory/objects/<model("reprocess_inventory.reprocess_inventory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reprocess_inventory.object', {
#             'object': obj
#         })
