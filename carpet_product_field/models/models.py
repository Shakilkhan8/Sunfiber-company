# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class carpet_product_field(models.Model):
#     _name = 'carpet_product_field.carpet_product_field'
#     _description = 'carpet_product_field.carpet_product_field'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
