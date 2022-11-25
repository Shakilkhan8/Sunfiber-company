from odoo import api, fields, models

class CarpetProductBarcode(models.Model):
    _inherit = 'carpet.barcode'

class CarpetSaleOrderModelInherit(models.Model):
    _inherit = 'sale.order'



