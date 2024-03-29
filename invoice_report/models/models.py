from odoo import api, fields, models


class InvoiceReportInheritModel(models.Model):
    _name = 'report.invoice_report.invoice_report_template_id'

    def _get_report_values(self, docids, data=None):

        inv = self.env['account.move'].search([('id', '=', docids)])
        rec_lst = []
        for line in inv.invoice_line_ids:
            if rec_lst:
                with_exist = list(filter(lambda item: item if item['design_id'] ==  line.product_id.categ_id.id and item['quality'] == line.product_id.carpet_quality_id.name and item['grade'] == line.product_id.carpet_grade_id.id  else None, rec_lst ))
                if with_exist:
                    with_exist[0]['amount'] += line.price_subtotal
                    with_exist[0]['length'] += line.product_id.carpet_length
                    with_exist[0]['sqf'] += line.quantity
                    with_exist[0]['quantity'] += line.sqf
                else:
                    g_name = line.product_id.carpet_grade_id.name if line.product_id.carpet_grade_id else ""

                    rec_lst.append({
                        'p_name': line.name,
                        'width': line.product_id.carpet_width,
                        'length': line.product_id.carpet_length,
                        'quality': line.product_id.carpet_quality_id.name,
                        'design': line.product_id.categ_id.name,
                        'design_id': line.product_id.categ_id.id,
                        'price': line.price_unit,
                        'quantity': line.sqf,
                        'sqf': line.quantity,
                        'amount': line.price_subtotal,
                        'grade': line.product_id.carpet_grade_id.id,
                        'grade_id': line.product_id.carpet_grade_id,
                    })

            else:
               g_name = line.product_id.carpet_grade_id.name if line.product_id.carpet_grade_id else ""
               rec_lst.append({
                   'p_name': line.name,
                   'width': line.product_id.carpet_width,
                   'length': line.product_id.carpet_length,
                   'quality': line.product_id.carpet_quality_id.name,
                   'design': line.product_id.categ_id.name ,
                   'design_id': line.product_id.categ_id.id,
                   'price': line.price_unit,
                   'quantity': line.sqf,
                   'sqf': line.quantity,
                   'amount': line.price_subtotal,
                   'grade': line.product_id.carpet_grade_id.id,
                   'grade_id': line.product_id.carpet_grade_id,

               })


        return {
            'record': rec_lst,
            'date': inv.invoice_date.strftime("%d- %m- %Y") if inv.invoice_date  else '-',
            'state': inv.state,
            'partner': inv.partner_id.name,
        }