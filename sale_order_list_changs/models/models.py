
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
