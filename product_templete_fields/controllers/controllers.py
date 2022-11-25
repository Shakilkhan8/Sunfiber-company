# -*- coding: utf-8 -*-
# from odoo import http


# class ProductTempleteFields(http.Controller):
#     @http.route('/product_templete_fields/product_templete_fields', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_templete_fields/product_templete_fields/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_templete_fields.listing', {
#             'root': '/product_templete_fields/product_templete_fields',
#             'objects': http.request.env['product_templete_fields.product_templete_fields'].search([]),
#         })

#     @http.route('/product_templete_fields/product_templete_fields/objects/<model("product_templete_fields.product_templete_fields"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_templete_fields.object', {
#             'object': obj
#         })
