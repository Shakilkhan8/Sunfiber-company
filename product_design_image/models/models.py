# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class product_design_image(models.Model):
#     _name = 'product_design_image.product_design_image'
#     _description = 'product_design_image.product_design_image'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
