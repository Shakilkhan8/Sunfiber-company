# -*- coding: utf-8 -*-
# from odoo import http


# class ProductDesignImage(http.Controller):
#     @http.route('/product_design_image/product_design_image', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_design_image/product_design_image/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_design_image.listing', {
#             'root': '/product_design_image/product_design_image',
#             'objects': http.request.env['product_design_image.product_design_image'].search([]),
#         })

#     @http.route('/product_design_image/product_design_image/objects/<model("product_design_image.product_design_image"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_design_image.object', {
#             'object': obj
#         })
