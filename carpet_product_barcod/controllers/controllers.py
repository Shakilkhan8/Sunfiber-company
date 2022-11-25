# -*- coding: utf-8 -*-
# from odoo import http


# class CarpetProductBarcod(http.Controller):
#     @http.route('/carpet_product_barcod/carpet_product_barcod', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/carpet_product_barcod/carpet_product_barcod/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('carpet_product_barcod.listing', {
#             'root': '/carpet_product_barcod/carpet_product_barcod',
#             'objects': http.request.env['carpet_product_barcod.carpet_product_barcod'].search([]),
#         })

#     @http.route('/carpet_product_barcod/carpet_product_barcod/objects/<model("carpet_product_barcod.carpet_product_barcod"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('carpet_product_barcod.object', {
#             'object': obj
#         })
