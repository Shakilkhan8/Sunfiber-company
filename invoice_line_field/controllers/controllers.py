# -*- coding: utf-8 -*-
# from odoo import http


# class InvoiceLineField(http.Controller):
#     @http.route('/invoice_line_field/invoice_line_field', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_line_field/invoice_line_field/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_line_field.listing', {
#             'root': '/invoice_line_field/invoice_line_field',
#             'objects': http.request.env['invoice_line_field.invoice_line_field'].search([]),
#         })

#     @http.route('/invoice_line_field/invoice_line_field/objects/<model("invoice_line_field.invoice_line_field"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_line_field.object', {
#             'object': obj
#         })
