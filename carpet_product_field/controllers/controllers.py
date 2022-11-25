# -*- coding: utf-8 -*-
# from odoo import http


# class CarpetProductField(http.Controller):
#     @http.route('/carpet_product_field/carpet_product_field', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/carpet_product_field/carpet_product_field/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('carpet_product_field.listing', {
#             'root': '/carpet_product_field/carpet_product_field',
#             'objects': http.request.env['carpet_product_field.carpet_product_field'].search([]),
#         })

#     @http.route('/carpet_product_field/carpet_product_field/objects/<model("carpet_product_field.carpet_product_field"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('carpet_product_field.object', {
#             'object': obj
#         })
