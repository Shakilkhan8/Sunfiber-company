from odoo import api, fields, models

class FiberSaleOrderModelInherit(models.Model):
    _inherit = 'sale.order'


class FiberSaleOrderLineModelInherit(models.Model):
    _inherit = 'sale.order.line'

    bales = fields.Float('Bales')
