from odoo import api, fields, models
from datetime import datetime
class ProductHistoryReport(models.TransientModel):
    _name = 'history.report.wizard'

    date = fields.Date('Select Date')

    def product_history_report(self):
        data = {}
        data['date'] = self.date

        return self.env.ref('carpet_product_field.product_hist_report_action_id').report_action(self, data= data)


class HistoryReportModel(models.AbstractModel):
    _name = 'report.carpet_product_field.product_hist_report_id'

    def _get_report_values(self, docids, data=None):
        product = self.env['product.template'].search([])
        flter = product.filtered(lambda item: item.create_date.date() == datetime.strptime(data['date'], '%Y-%m-%d').date())
        products = sorted(list(flter), key=lambda d: d['batch_number'])

        return {
            'product': products
        }
