from odoo import api, fields, models

class ProductDesignImage(models.Model):
    _inherit = 'product.category'

    design_image = fields.Binary(string=False)
    name = fields.Char('Name')