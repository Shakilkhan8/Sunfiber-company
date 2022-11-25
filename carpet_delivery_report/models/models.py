from odoo import api, fields, models
from operator import itemgetter
import operator
class DeliveryPackingModel(models.Model):
    _name = 'report.carpet_delivery_report.carpet_delivery_report'

    def _get_report_values(self, docids, data=None):
        order =  self.env['stock.picking'].browse(docids)

        data = []

        for line in order.move_ids_without_package:
                data.append({
                'design_name': line.product_id.categ_id.name,
                'quality_name': line.quality_id.name,
                'child_design': line.product_id.digital_print_child.name if line.product_id.digital_print_child.name else '-',
                'length': line.product_id.carpet_length,
                'width': line.product_id.carpet_width,
                'color': line.product_id.carpet_color,
                'grade': line.product_id.carpet_grade_id.name,
            })

        data.sort(key=operator.itemgetter('design_name', 'color'))
        name_sort = sorted(data, key=lambda i: i['design_name'])
        color_sort = sorted(name_sort, key=lambda i: (i['design_name'],i['color']))

        return {
            'record1': color_sort,
            'order': order,
            'number': order.name,
            'order_number': order.origin,
        }
