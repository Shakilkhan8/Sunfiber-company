import datetime

from odoo.http import request

request.env.cr
from odoo import api, fields, models
from datetime import datetime, date, timedelta


class InventoryReportWizard(models.TransientModel):
    _name = 'inventory.report.wizard'

    design_id = fields.Many2many('product.category' , domain= lambda self: [('company_id', '=', self.env.user.company_id.id)])

    def inventory_report_values(self):
        check_lst = []
        color_lst = []
        for rec in self.design_id.ids:
            product = self.env['product.template'].search([('categ_id', '=', rec)])
            for line in product:
                if check_lst:
                    dict_exist = list(filter(lambda i: i['cat_name'] == line.categ_id.name, check_lst))
                    if dict_exist:
                        color_check = list(filter(lambda item: item['color_name'] == line.carpet_color, dict_exist[0]['color']))
                        if color_check:
                            if line.carpet_grade_id.name == 'A':
                                color_check[0]['grade_a_color_qty'] += line.qty_available
                            else:
                                color_check[0]['grade_b_color_qty'] += line.qty_available
                        else:
                            dict_exist[0]['color'].append({
                                'color_name': line.carpet_color,
                                'grade_a_color_qty': line.qty_available,
                                'grade_b_color_qty': line.qty_available,
                            })
                    else:
                        check_lst.append({
                            'cat_name': line.categ_id.name,
                            'color': [],
                        })
                        color_add_lst = list(filter(lambda item: item['cat_name'] == line.categ_id.name, check_lst))
                        color_add_lst[0]['color'].append({
                            'color_name': line.carpet_color,
                            'grade_a_color_qty': line.qty_available,
                            'grade_b_color_qty': line.qty_available,
                        })
                else:
                    color_lst.append({
                        'color_name': line.carpet_color,
                        'grade_a_color_qty': line.qty_available,
                        'grade_b_color_qty': line.qty_available,
                    })

                    check_lst.append({
                        'cat_name': line.categ_id.name,
                        'color': color_lst,
                    })
        rec = {
            'record': check_lst
        }
        return self.env.ref('inventory_xlsx_report.inventory_report_action_id').report_action(self, data=rec)


class xlsReport(models.AbstractModel):
    _name = 'report.inventory_xlsx_report.xlsx_report_id'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):

        sheet = workbook.add_worksheet("Dail Stock Report")
        formate_two = workbook.add_format({'font_size': 12,'align': 'center', 'bold': True})
        formate_three = workbook.add_format({'font_size': 10,'align': 'center'})
        formates = workbook.add_format({'align': 'center', 'bold': True})
        sheet.set_column(2, 1, 25)

        sheet.merge_range('B3:K3', "Stock Daily Report", formates)
        sheet.merge_range('B4:K4', "UNIT-2 SUN FIBER PVT LTD.", formates)
        row = 6
        row_two = 8
        row_three = 9
        for record in data['record']:
            sheet.write(row, 1, record['cat_name'], formate_two)
            sheet.write(row + 1, 1, 'Rolls A', formate_two)
            sheet.write(row + 2, 1, 'Rolls B', formate_two)

            total_qty = 0
            total_b_qty = 0
            row_two +=1
            col = 3
            for line in record['color']:
                col +=2
                total_qty += line['grade_a_color_qty']
                total_b_qty += line['grade_b_color_qty']
                sheet.write(row, 2, 'Total', formate_two)
                sheet.write(row, col, line['color_name'], formate_two)
                sheet.write(row +1, col, line['grade_a_color_qty'], formate_three)
                sheet.write(row +2, col, line['grade_b_color_qty'], formate_three)
                sheet.write(row + 1, 2, total_qty, formate_three)
                sheet.write(row + 2, 2, total_b_qty, formate_three)

            res = 'B'+ str(row)+":"+'M'+ str(row)
            sheet.merge_range(res, '')
            row = row +4
            row_three = row_two + 1