from odoo import api, fields, models

class UserModelInherit(models.Model):
    _inherit = 'res.users'

    check_company = fields.Boolean('Check Company', default=True)


class CategoryInheritModel(models.Model):
    _inherit = 'product.category'

    def filter_category(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'Product Categories',
            'res_model': 'product.category',
            'view_mode': 'tree,form',
            'domain': [('company_id', '=', self.env.user.company_id.id)]
        }
