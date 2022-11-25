# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class carpet_color(models.Model):
#     _name = 'carpet_color.carpet_color'
#     _description = 'carpet_color.carpet_color'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
