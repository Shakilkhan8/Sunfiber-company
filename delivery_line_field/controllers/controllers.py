# -*- coding: utf-8 -*-
# from odoo import http


# class DeliveryLineField(http.Controller):
#     @http.route('/delivery_line_field/delivery_line_field', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delivery_line_field/delivery_line_field/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('delivery_line_field.listing', {
#             'root': '/delivery_line_field/delivery_line_field',
#             'objects': http.request.env['delivery_line_field.delivery_line_field'].search([]),
#         })

#     @http.route('/delivery_line_field/delivery_line_field/objects/<model("delivery_line_field.delivery_line_field"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delivery_line_field.object', {
#             'object': obj
#         })
