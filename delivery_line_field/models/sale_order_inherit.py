from datetime import timedelta

from odoo import api, fields, models


class SaleOrderModel(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrderModel, self).action_confirm()
        for rec in self:
            for line in rec.order_line:

                line.move_ids.length = line.product_id.carpet_length
                line.move_ids.quality_id = line.quality_id.id
                line.move_ids.design_id = line.design_id.id
                line.move_ids.width = line.product_id.carpet_width
                line.move_ids.color = line.product_id.carpet_color

        return res
