from odoo import api, fields, models
from odoo.exceptions import UserError


class CarpetColorModel(models.Model):
    _inherit = 'sale.order'

    color_line_id = fields.One2many('carpet.color.line', 'sale_order_id')
    currency_id = fields.Many2one('res.currency')
    total_price = fields.Monetary('Total Price', readonly=True, store=True)

    payment_received = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No')
    ])
    customer_note = fields.Text('Customer Note')
    sub_customer = fields.Char('Sub Customer')
    order_type = fields.Selection([
        ('Mix', 'Mix'),
        ('Print', 'Print'),
    ])
    delivery_confirm = fields.Selection([
        ('Non-Delivered', 'Non Delivered'),
        ('Delivered', 'Delivered'),
        ('One-Time', 'One Time'),
        ('Half-Paid', 'Half Paid')
    ])

    total_roll = fields.Float('Total roll')
    required_field_check = fields.Boolean(default=False)

    def default_get(self, fields_list):
        res = super(CarpetColorModel, self).default_get(fields_list)
        if self.env.user.check_company:
            res['required_field_check'] = True
        else:
            res['required_field_check'] = False
        return res

    # calculation of square feet in sale order line on the base of rolls and square feet formulla
    @api.onchange('order_line')
    def _onchange_oder_line(self):
        for rec in self.order_line:
            if self.env.user.check_company:
                rec.quality_id = rec.product_id.product_tmpl_id.carpet_quality_id.id
                rec.design_id = rec.product_id.product_tmpl_id.categ_id.id

            temp = self.env['product.template'].search([('id', '=', rec.product_id.product_tmpl_id.id)])
            if rec.product_uom_qty:
                if self.env.user.check_company:
                    if rec.product_id.digital_print_child:
                        rec.square_foot = rec.product_uom_qty * rec.product_id.product_tmpl_id.carpet_length * 3.281 * 12
                    else:
                        rec.square_foot = rec.product_uom_qty * rec.product_id.product_tmpl_id.carpet_length * 3.281 * 12

    @api.onchange('color_line_id')
    def _onchange_line_color(self):
        total_roll = 0
        for line in self.color_line_id:
            total_roll += line.total_qty
        self.total_roll = total_roll





class CarpetColorline(models.Model):
    _name = 'carpet.color.line'

    add_line_control = fields.Char()
    add_section_control = fields.Char()
    sequence = fields.Integer(string='Sequence', default=10)
    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False, help="Technical field for UX purpose.")

    square_foot = fields.Float('Square Foot')
    discount = fields.Float('Discount %')
    sale_order_id = fields.Many2one("sale.order")
    product_id = fields.Char("Product")
    design_id = fields.Many2one('product.category', required=True)
    child_design_id = fields.Many2one('digital.print.child', 'Child Design')
    child_image = fields.Binary('Child Image')
    check_design = fields.Boolean(default=False)
    quality_id = fields.Many2one('carpet.product.quality')
    color_0 = fields.Integer("0")
    color_1 = fields.Integer("1")
    color_1r = fields.Integer("1R")
    color_1d = fields.Integer("1D")
    color_1l = fields.Integer("1L")
    color_2 = fields.Integer("2")
    color_3 = fields.Integer("3")
    color_3l = fields.Integer("3L")
    color_3d = fields.Integer("3D")
    color_4 = fields.Integer("4")
    color_4l = fields.Integer("4L")
    color_5 = fields.Integer("5")
    color_5l = fields.Integer("5L")
    color_6 = fields.Integer("6")
    color_6d = fields.Integer("6D")
    color_6m = fields.Integer("6M")
    color_6l = fields.Integer("6L")
    color_7 = fields.Integer("7")
    color_7l = fields.Integer("7L")
    color_7r = fields.Integer("7R")
    color_8 = fields.Integer("8")
    color_9 = fields.Integer("9")
    color_10 = fields.Integer("10")
    color_10d = fields.Integer("10D")
    color_11 = fields.Integer("11")
    color_11r = fields.Integer("11R")
    color_11l = fields.Integer("11L")
    color_12 = fields.Integer("12")
    color_12r = fields.Integer("12R")
    color_13 = fields.Integer("13")
    color_13l = fields.Integer("13L")
    color_14 = fields.Integer("14")
    color_14d = fields.Integer("14D")
    color_15 = fields.Integer("15")
    color_16 = fields.Integer("16")
    color_17 = fields.Integer("17")
    color_17r = fields.Integer("17R")
    color_18 = fields.Integer("18")
    color_19 = fields.Integer("19")
    color_20 = fields.Integer("20")
    color_21 = fields.Integer("21")
    color_22 = fields.Integer("22")
    color_23 = fields.Integer("23")
    color_24 = fields.Integer("24")
    color_25 = fields.Integer("25")
    color_26 = fields.Integer("26")
    color_27 = fields.Integer("27")
    color_28 = fields.Integer("28")
    color_29 = fields.Integer("29")
    color_30 = fields.Integer("30")
    color_31 = fields.Integer("31")
    color_32 = fields.Integer("32")
    color_33 = fields.Integer("33")
    color_34 = fields.Integer("34")
    color_35 = fields.Integer("35")
    color_36 = fields.Integer("36")
    color_37 = fields.Integer("37")
    color_38 = fields.Integer("38")
    color_39 = fields.Integer("39")
    color_40 = fields.Integer("40")
    color_41 = fields.Integer("41")
    color_42 = fields.Integer("42")
    color_43 = fields.Integer("43")
    color_44 = fields.Integer("44")
    color_45 = fields.Integer("45")
    color_46 = fields.Integer("46")
    color_47 = fields.Integer("47")
    color_48 = fields.Integer("48")
    color_49 = fields.Integer("49")
    color_50 = fields.Integer("50")
    color_51 = fields.Integer("51")
    color_52 = fields.Integer("52")
    color_53 = fields.Integer("53")
    color_54= fields.Integer("54")
    color_55= fields.Integer("55")
    color_56= fields.Integer("56")
    color_57= fields.Integer("57")
    color_58= fields.Integer("58")
    color_59= fields.Integer("59")
    color_60= fields.Integer("60")
    color_61= fields.Integer("61")
    color_62= fields.Integer("62")
    color_63= fields.Integer("63")
    color_64= fields.Integer("64")
    color_65= fields.Integer("65")
    color_66= fields.Integer("66")
    color_67= fields.Integer("67")
    color_68= fields.Integer("68")
    color_69= fields.Integer("69")
    color_70= fields.Integer("70")
    color_71= fields.Integer("71")
    color_72= fields.Integer("72")
    color_73= fields.Integer("73")
    color_74= fields.Integer("74")
    color_75= fields.Integer("75")
    color_76= fields.Integer("76")
    color_77= fields.Integer("77")
    color_78= fields.Integer("78")
    color_79= fields.Integer("79")
    color_80= fields.Integer("80")
    color_81= fields.Integer("81")
    color_82= fields.Integer("82")
    color_83= fields.Integer("83")
    color_84= fields.Integer("84")
    color_85= fields.Integer("85")
    color_86= fields.Integer("86")
    color_87= fields.Integer("87")
    color_88= fields.Integer("88")
    color_89= fields.Integer("89")
    color_90= fields.Integer("90")
    color_91= fields.Integer("91")
    color_92= fields.Integer("92")
    color_93= fields.Integer("93")
    color_94= fields.Integer("94")
    color_95= fields.Integer("95")
    color_96= fields.Integer("96")
    color_97= fields.Integer("97")
    color_98= fields.Integer("98")
    color_99= fields.Integer("99")
    color_100= fields.Integer("100")

    total_qty = fields.Integer('Total qty', compute='_compute_total_roll')
    price_unit = fields.Float('Price', store=True)
    total_price = fields.Integer('Total Price', readonly=True, store=True, compute='_compute_total_price')
    image = fields.Binary("Image")
    product_name = fields.Char("Name")
    line_id = fields.Char('Line id')

    @api.onchange('child_design_id')
    def _onchange_child_design_id(self):
        if self.child_design_id:
            self.child_image = self.child_design_id.image

    @api.onchange('design_id')
    def _onchange_design_id(self):
        if self.design_id:
            if self.design_id.design_image:
                self.image = self.design_id.design_image

        # here we make child design required on the base of some specific category
        if self.design_id.name == 'Digital Printed' or self.design_id.name == 'Digital Printed with Felt' or self.design_id.name == 'Tufted Graphics' or self.design_id.name == 'Tufted Scroll':
            self.check_design = True
        else:
            self.check_design = False

    @api.depends('color_0','color_1','color_1d','color_1r','color_1l','color_2','color_3','color_3l','color_3d','color_4','color_4l','color_5','color_5l','color_6','color_6d','color_6m','color_6l','color_7','color_7l','color_7r','color_8','color_9','color_10','color_10d','color_11r','color_11l','color_12','color_12r','color_13','color_13l','color_14','color_14d','color_15','color_16','color_17','color_17r','color_18','color_19','color_20','color_21','color_22','color_23','color_24','color_25','color_26','color_27','color_28','color_29','color_30','color_31','color_32','color_33','color_34','color_35','color_36','color_37','color_38','color_39','color_40','color_41','color_42','color_43','color_44','color_45','color_46','color_47','color_48',
                 'color_49',
                 'color_50',
                 'color_51',
                 'color_52',
                 'color_53',
                 'color_54',
                 'color_55',
                 'color_56',
                 'color_57',
                 'color_58',
                 'color_59',
                 'color_60',
                 'color_61',
                 'color_62',
                 'color_63',
                 'color_64',
                 'color_65',
                 'color_66',
                 'color_67',
                 'color_68',
                 'color_69',
                 'color_70',
                 'color_71',
                 'color_72',
                 'color_73',
                 'color_74',
                 'color_75',
                 'color_76',
                 'color_77',
                 'color_78',
                 'color_79',
                 'color_80',
                 'color_81',
                 'color_82',
                 'color_83',
                 'color_84',
                 'color_85',
                 'color_86',
                 'color_87',
                 'color_88',
                 'color_89',
                 'color_90',
                 'color_91',
                 'color_92',
                 'color_93',
                 'color_94',
                 'color_95',
                 'color_96',
                 'color_97',
                 'color_98',
                 'color_99',
                 'color_100',
                 )
    def _compute_total_roll(self):
        for line in self:
            line.total_qty= line.color_0 + line.color_1 + line.color_2 + line.color_3 + line.color_4 + line.color_5 + line.color_6 + line.color_7 + line.color_8 + line.color_9 + line.color_10 + line.color_11 + line.color_12 + line.color_13 + line.color_14 + line.color_15 + line.color_16 + line.color_17 + line.color_18 + line.color_19 + line.color_20 + line.color_21 + line.color_22 + line.color_23 + line.color_24 + line.color_25 + line.color_26 + line.color_27 + line.color_28 + line.color_29 + line.color_30 + line.color_31 + line.color_32 + line.color_33 + line.color_34 + line.color_35 + line.color_36 + line.color_37 + line.color_38 + line.color_39 + line.color_40 + line.color_41 + line.color_42 + line.color_43 + line.color_44 + line.color_45 + line.color_46 + line.color_47 + line.color_48 + line.color_49 + line.color_50 + line.color_51 + line.color_52 + line.color_53 + line.color_54 + line.color_55 + line.color_56 + line.color_57 + line.color_58 + line.color_59 + line.color_60 + line.color_61 + line.color_62 + line.color_63 + line.color_64 + line.color_65 + line.color_66 + line.color_67 + line.color_68 + line.color_69 + line.color_70 + line.color_71 + line.color_72 + line.color_73 + line.color_74 + line.color_75 + line.color_76 + line.color_77 + line.color_78 + line.color_79 + line.color_80 + line.color_81+ line.color_82 + line.color_83 + line.color_84 + line.color_85 + line.color_86 + line.color_87 + line.color_88 + line.color_89 + line.color_90 + line.color_91 + line.color_91 + line.color_92 + line.color_94 + line.color_95 + line.color_96 + line.color_97 + line.color_98 + line.color_99 + line.color_100 + line.color_1d + line.color_1l + line.color_1r + line.color_3d + line.color_3l + line.color_4l + line.color_5l + line.color_6l + line.color_6d + line.color_6m + line.color_7l + line.color_7r + line.color_10d + line.color_11l + line.color_11r + line.color_12r + line.color_13l + line.color_14d + line.color_17r
            line.square_foot = line.total_qty * 36 * 3.281 * 12

    @api.depends('price_unit', 'square_foot')
    def _compute_total_price(self):
        for line in self:
            line.total_price = line.square_foot * line.price_unit

    @api.onchange('design_id','quality_id')
    def _onchange_des_qual(self):
        # if both design and quality selected then we concatenate the both to create product name

        for line in self:
            if line.design_id and line.quality_id:
                if line.child_design_id:
                    line.product_id = line.design_id.name + " / " + str(
                        line.child_design_id.name) + " / " + line.quality_id.name
                else:
                    line.product_id = str(line.design_id.name) + " / " + str(line.quality_id.name)

    @api.onchange('child_design_id')
    def _onchange_design_quality(self):
        # if both design and quality selected then we concatenate the both to create product name
        for line in self:
                if line.child_design_id and line.design_id and line.quality_id:
                    line.product_id = line.design_id.name + " / " + str(
                        line.child_design_id.name) + " / " + line.quality_id.name
                else:
                    line.product_id = ""


class InheritSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    quality_id = fields.Many2one('carpet.product.quality', 'Quality')
    design_id = fields.Many2one('product.category', 'Design')
    square_foot = fields.Float('Square Foot')
    delivered = fields.Date('Delivered')
    price_subtotal = fields.Float(store=1)
    price_unit = fields.Float('Price Unit', store=True)

    @api.depends('price_unit')
    def _compute_subtotal(self):
        for line in self:
            if self.env.user.check_company:
                line.price_subtotal = line.price_unit * line.square_foot


    def calculate_bales(self, price_unit, product_qty):
        return price_unit * product_qty

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty,
                                            product=line.product_id, partner=line.order_id.partner_shipping_id)
            subtotal = 0.0
            if not self.env.user.check_company:
                    subtotal = self.calculate_bales(line.price_unit, line.product_uom_qty)
            else:
               subtotal = line.price_unit * line.square_foot

            line.update({
                'price_tax': taxes['total_included'] - taxes['total_excluded'],
                'price_total': taxes['total_included'],
                'price_subtotal': subtotal,
                'bales': (line.product_uom_qty/240)
            })
            if self.env.context.get('import_file', False) and not self.env.user.user_has_groups(
                    'account.group_account_manager'):
                line.tax_id.invalidate_cache(['invoice_repartition_line_ids'], [line.tax_id.id])


class StockMoveModel(models.Model):
    _inherit = 'stock.move.line'

    quality_id = fields.Many2one('carpet.product.quality')
    design_id = fields.Many2one('product.category')


class StockMoveModel(models.Model):
    _inherit = 'stock.move'

    quality_id = fields.Many2one('carpet.product.quality')
    design_id = fields.Many2one('product.category')
