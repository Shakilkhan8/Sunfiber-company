# -*- coding: utf-8 -*-
# from odoo import http


# class ChildDesign(http.Controller):
#     @http.route('/child_design/child_design', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/child_design/child_design/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('child_design.listing', {
#             'root': '/child_design/child_design',
#             'objects': http.request.env['child_design.child_design'].search([]),
#         })

#     @http.route('/child_design/child_design/objects/<model("child_design.child_design"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('child_design.object', {
#             'object': obj
#         })
