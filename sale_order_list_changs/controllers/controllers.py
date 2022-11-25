# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderListChangs(http.Controller):
#     @http.route('/sale_order_list_changs/sale_order_list_changs', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_list_changs/sale_order_list_changs/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_list_changs.listing', {
#             'root': '/sale_order_list_changs/sale_order_list_changs',
#             'objects': http.request.env['sale_order_list_changs.sale_order_list_changs'].search([]),
#         })

#     @http.route('/sale_order_list_changs/sale_order_list_changs/objects/<model("sale_order_list_changs.sale_order_list_changs"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_list_changs.object', {
#             'object': obj
#         })
