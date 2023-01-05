from odoo import api, fields, models
from operator import itemgetter
import operator


class DeliveryPackingModel(models.Model):
    _name = 'report.carpet_delivery_report.carpet_delivery_report'

    def _get_report_values(self, docids, data=None):
        order = self.env['stock.picking'].browse(docids)
        data = []
        quality_base_list = []
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

            if quality_base_list:
                with_exist = [i for i in quality_base_list if i['quality_id'].id == line.quality_id.id and i[
                    'design_id'].id == line.product_id.categ_id.id and i['grade'].id == line.product_id.carpet_grade_id.id]
                if with_exist:
                    with_exist[0]['length'] += line.product_id.carpet_length
                    with_exist[0]['qty'] += line.product_uom_qty
                else:
                    quality_base_list.append({
                        'quality_id': line.quality_id,
                        'length': line.product_id.carpet_length,
                        'design_id': line.product_id.categ_id,
                        'grade': line.product_id.carpet_grade_id,
                        'qty': line.product_uom_qty,
                    })

            else:
                quality_base_list.append({
                    'quality_id': line.quality_id,
                    'length': line.product_id.carpet_length,
                    'design_id': line.product_id.categ_id,
                    'grade': line.product_id.carpet_grade_id,
                    'qty': line.product_uom_qty,
                })

        data.sort(key=operator.itemgetter('design_name', 'color'))
        name_sort = sorted(data, key=lambda i: i['design_name'])
        color_sort = sorted(name_sort, key=lambda i: (i['design_name'], i['color']))

        return {
            'record1': color_sort,
            'order': order,
            'number': order.name,
            'date_done': order.date_done.strftime("%d- %m- %Y") if order.date_done  else '-',
            'state': order.state,
            'order_number': order.origin,
            'quality_based_list': quality_base_list
        }
