from odoo import api, fields, models

class AccountMoveInherit(models.Model):
    _inherit = 'account.move'


    select_items = fields.Boolean(defult=False)

    @api.onchange('select_items')
    def _onchange_items(self):
        for line in self.line_ids:
            if self.select_items:
                line.check_item = True
            else:
                line.check_item = False

    def delete_items(self):
        for line in self.line_ids:
            if line.check_item:
                line.unlink()

class AccountMoveLineInherit(models.Model):
    _inherit = 'account.move.line'

    check_item = fields.Boolean(default=False)
