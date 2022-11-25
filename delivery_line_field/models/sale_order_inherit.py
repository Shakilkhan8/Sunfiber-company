import datetime

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SaleOrderModel(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        self.confirmation_date = datetime.datetime.now().date()
        res = super(SaleOrderModel, self).action_confirm()
        for rec in self:
            for line in rec.order_line:
                line.move_ids.length = line.product_id.carpet_length
                line.move_ids.quality_id = line.quality_id.id
                line.move_ids.design_id = line.design_id.id
                line.move_ids.width = line.product_id.carpet_width
                line.move_ids.color = line.product_id.carpet_color
                line.move_ids.bales = line.bales if not self.env.user.check_company else 0.0

                # updating product bales during confirmation of sale order
                if not self.env.user.check_company:
                    if line.product_id.bales < line.bales:
                        raise ValidationError('Bales on hand of %s' % line.product_id.name + ' are less than available bales !')
                    else:
                        line.product_id.bales = line.product_id.bales - line.bales

        return res
