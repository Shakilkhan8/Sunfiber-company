import re
from datetime import datetime, timedelta

from odoo import api, fields, models, _
from odoo.osv.expression import expression


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

    @api.model
    def create(self, vals):
        res = super(CarpetProductFields, self).create(vals)
        if res['batch_number']:
            product_product = self.env['product.product'].search([('product_tmpl_id', '=', res.id)])
            if product_product:
                for rec in product_product:
                    rec.batch_number = res['batch_number']
        return res

    # def write(self, vals):
    #     res = super(InheritProductTemplate, self).write(vals)
    #     if vals.get('customer_ids'):
    #         product_product = self.env['product.product'].search([('product_tmpl_id', '=', self.id)])
    #         if product_product:
    #             for rec in product_product:
    #                 rec.customer_ids = vals.get('customer_ids')
    #     return res

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = [] if args is None else args.copy()
        if not (name == '' and operator == 'ilike'):
            args += ['|', '|',
                     ('name', operator, name),
                     ('batch_number', operator, name),
                     ('barcode', operator, name)
                     ]
        return super(CarpetProductFields, self)._name_search(name=name, args=args, operator=operator,
                                                               limit=limit, name_get_uid=name_get_uid)


class ProductProductInherit(models.Model):
    _inherit = 'product.product'

    batch_number = fields.Char('Batch Number')

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if not (name == '' and operator == 'ilike'):
            args += ['|', '|',
                     ('name', operator, name),
                     ('batch_number', operator, name),
                     ('barcode', operator, name)
                     ]
        return super(ProductProductInherit, self)._name_search(name=name, args=args, operator=operator,
                                                               limit=limit, name_get_uid=name_get_uid)

class DigitalPrintChildCategory(models.Model):
    _name = 'digital.print.child'

    name = fields.Char('Child Design')
    image = fields.Binary('Image')
    categ_id = fields.Many2one('product.category')
    combine_design_image = fields.Binary('Combine Design Image')
