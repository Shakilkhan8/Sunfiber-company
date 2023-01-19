import datetime

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

    dispatch_date = fields.Date('Dispatch Date')
    confirmation_date = fields.Date('Confirmation Date')
    total_sqf = fields.Float('Total SQF', compute='_compute_total_sqf')


    @api.depends('order_line.square_foot')
    def _compute_total_sqf(self):
        for rec in self:
            total = 0.0
            for line in rec.order_line:
                total += line.square_foot
            rec.total_sqf = total


    def action_dispatch(self):
        self.dispatch_date = datetime.datetime.now().date()
        self.state = 'dispatch'

    def action_confirm(self):
        self.confirmation_date = datetime.datetime.now().date()
        res = super(SaleOrderListView, self).action_confirm()
        self.state = 'sale'
        return res








