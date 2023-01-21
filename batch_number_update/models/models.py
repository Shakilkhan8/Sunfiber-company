from odoo import api, fields, models

class ProductTempInherit(models.Model):
    _inherit = 'product.template'


    def update_batch_no(self):
        temp = self.env['product.template'].search([])
        for line in temp:
            p = self.env['product.product'].search([('product_tmpl_id', '=', line.id)],limit=1)
            p.batch_number = line.batch_number
