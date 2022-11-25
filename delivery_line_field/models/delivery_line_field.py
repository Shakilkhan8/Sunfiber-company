from datetime import timedelta

from odoo import api, fields, models

class DeliveryLineField(models.Model):
    _inherit = 'stock.picking'


class StockMoveInherit(models.Model):
    _inherit = 'stock.move'

    design_id = fields.Many2one('product.category')
    quality_id = fields.Many2one('carpet.product.quality')
    length = fields.Float('Length')
    width = fields.Float('Width')
    color = fields.Char('Color')



