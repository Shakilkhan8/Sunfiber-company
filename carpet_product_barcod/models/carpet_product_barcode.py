from odoo import api, fields, models
from random import randrange, random, randint
from odoo.exceptions import UserError, ValidationError


class CarpetProductBarcode(models.Model):
    _name = 'carpet.barcode'
    _rec_name = 'categ_id'

    categ_id = fields.Many2one('product.category', 'Design *', required=True)
    carpet_color = fields.Char('Color *', required=True)
    carpet_quality = fields.Many2one("carpet.product.quality", "Quality *", requried=True)
    location_id = fields.Many2one('stock.location', "Location *",   readonly=True, domain=[('usage', '=', 'internal')])
    meters = fields.Float('Enter Meters *', required=True)
    width = fields.Float(default= 3.66, required=True)
    carpet_grade_id = fields.Many2one('carpet.grade', 'Carpet Grade *', required=True)
    digital_print_child = fields.Many2one('digital.print.child', 'Child')
    check = fields.Boolean(default=False)

    @api.model
    def default_get(self, fields_list):
        res = super(CarpetProductBarcode, self).default_get(fields_list)
        res['location_id'] = self.env['stock.location'].search([('complete_name', '=', 'FSB/Stock')]).id
        return res

    @api.onchange('categ_id')
    def _onchange_category(self):
        if self.categ_id.name == 'Digital Printed' or self.categ_id.name == 'Digital Printed with Felt' or self.categ_id.name == 'Tufted Graphics' or self.categ_id.name == 'Tufted Scroll':
            self.check = True
        else:
            self.check = False


    def create_product_template(self):
        l = []
        if self.categ_id.name == 'Digital Printed' or self.categ_id.name == 'Digital Printed with Felt' or self.categ_id.name == 'Tufted Graphics' or self.categ_id.name == 'Tufted Scroll':
            name = self.categ_id.name + " / " + self.digital_print_child.name + " / "+ self.carpet_color + " / " + str(
                self.meters) + "m" + " / " + self.carpet_quality.display_name

        else:
            name = self.categ_id.name + " / " + self.carpet_color+ " / " + str(
            self.meters) + "m" + " / " + self.carpet_quality.display_name
            self.digital_print_child = False
        comp = self.env['res.company'].browse(self._context.get('allowed_company_ids'))
        comp = comp.filtered(lambda i: 'Sun Fiber' in i.name)
        pro = self.env['product.template'].create({
            'name': name,
            'digital_print_child': self.digital_print_child.id,
            'carpet_color': self.carpet_color,
            'carpet_quality_id': self.carpet_quality.id,
            'carpet_grade_id': self.carpet_grade_id.id,
            'detailed_type': 'product',
            'carpet_length': self.meters,
            'carpet_width': self.width,
            'categ_id': self.categ_id.id,
            'barcode': randint(00000000000, 99999999999),
            'company_id': comp.id if 'Sun Fiber' in comp.name else None

        })
        pp = self.env['product.product'].search([('product_tmpl_id', '=', pro.id)])
        loc = self.env['stock.quant'].search([('company_id', '=', comp.id)])
        stock = self.env['stock.quant'].create({
            'inventory_quantity_set': True,
            'product_id': pp.id,
            'quantity': 1,
            'inventory_quantity': 1,
            'location_id': self.location_id.id
        })

        data = {
            'name': pro.name,
            'barcode': pro.barcode,
        }

        return self.env.ref('carpet_product_barcod.product_barcode_action_id').report_action(self, data=data)


class BarcodeLabelPrint(models.AbstractModel):
    _name = 'report.carpet_product_barcod.product_barcode_template_id'

    def _get_report_values(self, docids, data=None):
        rec = self.env['carpet.barcode'].search([('id', '=', self._context.get('active_id'))])

        if rec.digital_print_child:
            product_name = rec.categ_id.name + " / " + rec.digital_print_child.name + " / " + rec.carpet_color + " / " + str(rec.meters) + "m" + " / " + rec.carpet_quality.display_name
        else:
            product_name = rec.categ_id.name + " / " + rec.carpet_color + " / " + str(rec.meters) + "m" + " / " + rec.carpet_quality.display_name

        return {
            'product_name': product_name,
            'barcode': data['barcode']
        }
