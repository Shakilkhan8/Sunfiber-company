from odoo import api, fields, models

class CarpetGradesModel(models.Model):
    _name = 'carpet.grade'

    name = fields.Char("Carpet Grades")