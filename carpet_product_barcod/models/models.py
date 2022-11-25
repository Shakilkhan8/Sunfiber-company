# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class carpet_product_barcod(models.Model):
#     _name = 'carpet_product_barcod.carpet_product_barcod'
#     _description = 'carpet_product_barcod.carpet_product_barcod'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
