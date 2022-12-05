# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BiPrintInheritJournal(models.Model):
    _inherit = 'account.move.line'

    bi_source = fields.Char(string='Source', required=False)
    bi_memo = fields.Char(string='Memo', required=False)
