import requests

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        res.update({
            'sqf': self.product_uom_qty,
            'quality_id': self.quality_id.id,
            'quantity': self.square_foot
        })
        return res


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    sqf = fields.Float('SQ Feet', store=True)



