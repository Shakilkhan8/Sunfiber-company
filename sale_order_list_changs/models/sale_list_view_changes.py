from odoo import api, fields, models

class SaleOrderListView(models.Model):
    _inherit = 'sale.order'

    receive_date = fields.Datetime('Receive Date')
    expect_date = fields.Datetime('Expected Date')
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('dispatch', 'Dispatch'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    def action_dispatch(self):
        self.state = 'dispatch'


