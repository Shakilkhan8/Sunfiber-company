from odoo import api, fields, models


class AccountMoveModelInherit(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, vals_list):
        res = super(AccountMoveModelInherit, self).create(vals_list)
        order = self.env['sale.order'].search([('name', '=', res['invoice_origin'])])
        order.invoice_status = 'invoiced'
        return res

    # @api.onchange('invoice_line_ids')
    # def _onchange_line(self):
    #     check_lst = []
    #     for line in self.invoice_line_ids:
    #
    #         if check_lst:
    #             check_exist = list(filter(lambda item: item['design_id'] == line.product_id.categ_id.id and item['quality_id'] == line.product_id.carpet_quality_id.id, check_lst))
    #             if check_exist:
    #                 line['price_unit'] = check_exist[0]['price_unit']
    #             else:
    #                 check_lst.append({
    #                     'design_id': line.product_id.categ_id.id,
    #                     'quality_id': line.product_id.carpet_quality_id.id,
    #                     'price_unit': line.price_unit,
    #                 })
    #         else:
    #             check_lst.append({
    #                 'design_id': line.product_id.categ_id.id,
    #                 'quality_id': line.product_id.carpet_quality_id.id,
    #                 'price_unit': line.price_unit,
    #             })
    #
    #         line.price_subtotal = line.price_unit * line.product_id.carpet_length * 12 * 3.281
    #         line.sqf = line.product_id.carpet_length * 12 * 3.281

class InvoiceInheritModel(models.Model):
    _inherit = 'account.move.line'

    quality_id = fields.Many2one("carpet.product.quality")
    discount = fields.Float('Discount')
    sqf = fields.Float('Sqf')
