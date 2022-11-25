from odoo import api, fields, models

class UserModelInherit(models.Model):
    _inherit = 'res.users'

    check_company = fields.Boolean('Check Company', default=True)