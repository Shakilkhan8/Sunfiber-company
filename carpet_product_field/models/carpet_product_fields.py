from datetime import datetime,timedelta

from odoo import api, fields, models


class CarpetProductFields(models.Model):
    _inherit = 'product.template'


    carpet_color = fields.Char("Color")
    unit_of_measure = fields.Char("Unit of Measure", default='m', readonly=True)
    carpet_length = fields.Float("Length")
    carpet_width = fields.Float("Width")
    carpet_grade_id = fields.Many2one('carpet.grade', 'Grade')
    carpet_quality_id = fields.Many2one('carpet.product.quality', 'Quality')
    categ_id = fields.Many2one(
        'product.category', 'Product Design',
        change_default=True, group_expand='_read_group_categ_id',
        required=True, help="Select category for the current product")
    digital_print_child = fields.Many2one('digital.print.child')
    batch_number = fields.Text('Batch Number')

    def show_product(self):
        product = self.search([])
        p = product.filtered(lambda item: item.create_date.date() ==  datetime.now().date().today() - timedelta(days=1))
        return {
            'name': 'Product Template',
            'view_mode': 'tree',
            'view_id': False,
            'res_model': 'product.template',
            'domain': [('id', 'in', p.ids)],
            'type': 'ir.actions.act_window',
        }

class DigitalPrintChildCategory(models.Model):
    _name = 'digital.print.child'

    name = fields.Char('Child Design')
    image = fields.Binary('Image')
    categ_id = fields.Many2one('product.category')
    combine_design_image = fields.Binary('Combine Design Image')
