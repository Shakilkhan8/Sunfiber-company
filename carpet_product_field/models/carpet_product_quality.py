from odoo import api, fields, models


class CarpetQualityModel(models.Model):
    _name = 'carpet.product.quality'

    name = fields.Char('Quality Name')