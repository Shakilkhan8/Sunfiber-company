# -*- coding: utf-8 -*-
# from odoo import http


# class CarpetColor(http.Controller):
#     @http.route('/carpet_color/carpet_color', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/carpet_color/carpet_color/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('carpet_color.listing', {
#             'root': '/carpet_color/carpet_color',
#             'objects': http.request.env['carpet_color.carpet_color'].search([]),
#         })

#     @http.route('/carpet_color/carpet_color/objects/<model("carpet_color.carpet_color"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('carpet_color.object', {
#             'object': obj
#         })
