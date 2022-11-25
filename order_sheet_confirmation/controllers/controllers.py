# -*- coding: utf-8 -*-
# from odoo import http


# class OrderSheetConfirmation(http.Controller):
#     @http.route('/order_sheet_confirmation/order_sheet_confirmation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/order_sheet_confirmation/order_sheet_confirmation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('order_sheet_confirmation.listing', {
#             'root': '/order_sheet_confirmation/order_sheet_confirmation',
#             'objects': http.request.env['order_sheet_confirmation.order_sheet_confirmation'].search([]),
#         })

#     @http.route('/order_sheet_confirmation/order_sheet_confirmation/objects/<model("order_sheet_confirmation.order_sheet_confirmation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('order_sheet_confirmation.object', {
#             'object': obj
#         })
