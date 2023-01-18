from datetime import datetime,timedelta

from odoo import api, fields, models


class CarpetProductFields(models.Model):
    _inherit = 'product.template'


    carpet_color = fields.Char("Color")
    unit_of_measure = fields.Char("Unit of Measure", default='m', readonly=True)
    carpet_length = fields.Float("Length")
    carpet_width = fields.Float("Width")
    carpet_grade_id = fields.Many2one('carpet.grade', 'Grade')
    carpet_quality_id = fields.Many2one('carpet.product.quality', 'Quality')
    categ_id = fields.Many2one(
        'product.category', 'Product Design',
        change_default=True, group_expand='_read_group_categ_id',
        required=True, help="Select category for the current product")
    digital_print_child = fields.Many2one('digital.print.child')
    batch_number = fields.Text('Batch Number')


class ProductProductInherit(models.Model):
    _inherit = 'product.product'

    def name_get(self):
        # TDE: this could be cleaned a bit I think

        def _name_get(d):
            name = d.get('name', '')
            code = self._context.get('display_default_code', True) and d.get('default_code', False) or False
            batch = d.get('batch_number') if d.get('batch_number') else ""
            if code or d.get('batch_number')  :
                name = '%s [%s] %s' % (batch, code, name)
            return (d['id'], name)

        partner_id = self._context.get('partner_id')
        if partner_id:
            partner_ids = [partner_id, self.env['res.partner'].browse(partner_id).commercial_partner_id.id]
        else:
            partner_ids = []
        company_id = self.env.context.get('company_id')

        # all user don't have access to seller and partner
        # check access and use superuser
        self.check_access_rights("read")
        self.check_access_rule("read")

        result = []

        # Prefetch the fields used by the `name_get`, so `browse` doesn't fetch other fields
        # Use `load=False` to not call `name_get` for the `product_tmpl_id`
        self.sudo().read(['name', 'default_code', 'product_tmpl_id'], load=False)

        product_template_ids = self.sudo().mapped('product_tmpl_id').ids

        if partner_ids:
            supplier_info = self.env['product.supplierinfo'].sudo().search([
                ('product_tmpl_id', 'in', product_template_ids),
                ('name', 'in', partner_ids),
            ])
            # Prefetch the fields used by the `name_get`, so `browse` doesn't fetch other fields
            # Use `load=False` to not call `name_get` for the `product_tmpl_id` and `product_id`
            supplier_info.sudo().read(['product_tmpl_id', 'product_id', 'product_name', 'product_code'], load=False)
            supplier_info_by_template = {}
            for r in supplier_info:
                supplier_info_by_template.setdefault(r.product_tmpl_id, []).append(r)
        for product in self.sudo():
            variant = product.product_template_attribute_value_ids._get_combination_name()

            name = variant and "%s %s (%s)" % (product.name, product.batch_number, variant) or product.name
            sellers = self.env['product.supplierinfo'].sudo().browse(self.env.context.get('seller_id')) or []
            if not sellers and partner_ids:
                product_supplier_info = supplier_info_by_template.get(product.product_tmpl_id, [])
                sellers = [x for x in product_supplier_info if x.product_id and x.product_id == product]
                if not sellers:
                    sellers = [x for x in product_supplier_info if not x.product_id]
                # Filter out sellers based on the company. This is done afterwards for a better
                # code readability. At this point, only a few sellers should remain, so it should
                # not be a performance issue.
                if company_id:
                    sellers = [x for x in sellers if x.company_id.id in [company_id, False]]
            if sellers:
                for s in sellers:
                    seller_variant = s.product_name and (
                            variant and "%s %s (%s)" % (s.product_name, product.batch_number, variant) or s.product_name
                    ) or False
                    mydict = {
                        'id': product.id,
                        'name': seller_variant or name,
                        'default_code': s.product_code or product.default_code,
                        'batch_number': product.batch_number,
                    }
                    temp = _name_get(mydict)
                    if temp not in result:
                        result.append(temp)
            else:
                mydict = {
                    'id': product.id,
                    'name': name,
                    'default_code': product.default_code,
                    'batch_number': product.batch_number,
                }
                result.append(_name_get(mydict))
        return result


class DigitalPrintChildCategory(models.Model):
    _name = 'digital.print.child'

    name = fields.Char('Child Design')
    image = fields.Binary('Image')
    categ_id = fields.Many2one('product.category')
    combine_design_image = fields.Binary('Combine Design Image')
