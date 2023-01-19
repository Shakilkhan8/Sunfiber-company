# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sale_order_list_changs(models.Model):
#     _name = 'sale_order_list_changs.sale_order_list_changs'
#     _description = 'sale_order_list_changs.sale_order_list_changs'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    carpet_length = fields.Char("Carpet Length", readonly=True)
    square_foot = fields.Char("Saquare Foot", readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['carpet_length'] = ", t.carpet_length as carpet_length"
        fields['square_foot'] = ", l.square_foot as square_foot"
        # fields['test'] = ", SUM(10)"
        groupby += ",t.carpet_length"
        groupby += ",l.square_foot"
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
