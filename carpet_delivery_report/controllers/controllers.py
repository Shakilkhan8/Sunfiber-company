# -*- coding: utf-8 -*-
# from odoo import http


# class CarpetDeliveryReport(http.Controller):
#     @http.route('/carpet_delivery_report/carpet_delivery_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/carpet_delivery_report/carpet_delivery_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('carpet_delivery_report.listing', {
#             'root': '/carpet_delivery_report/carpet_delivery_report',
#             'objects': http.request.env['carpet_delivery_report.carpet_delivery_report'].search([]),
#         })

#     @http.route('/carpet_delivery_report/carpet_delivery_report/objects/<model("carpet_delivery_report.carpet_delivery_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('carpet_delivery_report.object', {
#             'object': obj
#         })
