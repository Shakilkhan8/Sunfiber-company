from odoo import api, fields, models

class ProductCategoryModel(models.Model):
    _inherit = 'product.category'

    quality_id = fields.Many2many('carpet.product.quality')