from odoo import api, fields, models

class ManualPackingListModel(models.TransientModel):
    _name = 'report.order_sheet_confirmation.manual_packing_list_id'

    def _get_report_values(self, docids, data=None):
        order = self.env['sale.order'].browse(docids)

        lst = []
        data_list = []
        for item in order.color_line_id:
            if item.color_0 !=0:
                count = item.color_0
                while count !=0:
                    lst.append({
                        'color': '0',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id if item.child_design_id else '-'
                    })
                    count -= 1


            if item.color_1 !=0:
                count = item.color_1
                while count !=0:
                    lst.append({
                        'color':'1',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1

            if item.color_1r !=0:
                count = item.color_1r
                while count !=0:
                    lst.append({
                        'color':'1R',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1

            if item.color_1d !=0:
                count = item.color_1d
                while count !=0:
                    lst.append({
                        'color': '1D',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_1l != 0:
                count = item.color_1l
                while count!= 0:
                    lst.append({
                        'color': '1L',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_2 !=0:
                count = item.color_2
                while count !=0:
                    lst.append({
                        'color': '2',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1

            if item.color_3 !=0:
                count = item.color_3
                while count !=0:
                    lst.append({
                        'color': '3',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_3d != 0:
                count = item.color_3d
                while count != 0:
                    lst.append({
                        'color': '3D',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_3l != 0:
                count = item.color_3l
                while count != 0:
                    lst.append({
                        'color': '3L',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_4 !=0:
                count = item.color_4
                while count !=0:
                    lst.append({
                        'color': '4',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_4l !=0:
                count = item.color_4l
                while count !=0:
                    lst.append({
                        'color': '4L',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1

            if item.color_5 !=0:
                count = item.color_5
                while count !=0:
                    lst.append({
                        'color': '5',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_5l !=0:
                count = item.color_5l
                while count !=0:
                    lst.append({
                        'color': '5L',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1

            if item.color_6 !=0:
                count = item.color_6
                while count !=0:
                    lst.append({
                        'color': '6',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_6d !=0:
                count = item.color_6d
                while count !=0:
                    lst.append({
                        'color': '6D',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count-=1
            if item.color_6m !=0:
                count = item.color_6m
                while count !=0:
                    lst.append({
                        'color': '6M',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_6l !=0:
                count = item.color_6l
                while count !=0:
                    lst.append({
                        'color': '6L',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1

            if item.color_7 !=0:
                count = item.color_7
                while count !=0:
                    lst.append({
                        'color': '7',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_7l !=0:
                count = item.color_7l
                while count !=0:
                    lst.append({
                        'color': '7L',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_7r !=0:
                count = item.color_7r
                while count !=0:
                    lst.append({
                        'color': '7R',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1

            if item.color_8 !=0:
                count = item.color_8
                while count !=0:
                    lst.append({
                        'color': '8',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1

            if item.color_9 !=0:
                count = item.color_9
                while count !=0:
                    lst.append({
                        'color': '9',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_10 !=0:
                count = item.color_10
                while count!=0:
                    lst.append({
                        'color': '10',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_10d !=0:
                count = item.color_10d
                while count !=0:
                    lst.append({
                        'color': '10D',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1

            if item.color_11 !=0:
                count = item.color_11
                while count !=0:
                    lst.append({
                        'color': '11',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_11l !=0:
                count = item.color_11l
                while count !=0:
                    lst.append({
                        'color': '11L',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_11r !=0:
                count = item.color_11r
                while count !=0:
                    lst.append({
                        'color': '11R',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1

            if item.color_12 !=0:
                count = item.color_12
                while  count !=0:
                    lst.append({
                        'color': '12',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_12r !=0:
                count = item.color_12r
                while count !=0:
                    lst.append({
                        'color': '12R',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1

            if item.color_13 !=0:
                count = item.color_13
                while count !=0:
                    lst.append({
                        'color': '13',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_13l !=0:
                count = item.color_13l
                while count !=0:
                    lst.append({
                        'color': '13L',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1

            if item.color_14 !=0:
                count = item.color_14
                while count !=0:
                    lst.append({
                        'color': '14',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_14d != 0:
                count = item.color_14d
                while count != 0:
                    lst.append({
                        'color': '14D',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1

            if item.color_15 !=0:
                count = item.color_15
                while count !=0:
                    lst.append({
                        'color': '15',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_16 !=0:
                count = item.color_16
                while count !=0:
                    lst.append({
                        'color': '16',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_17 !=0:
                count = item.color_17
                while count !=0:
                    lst.append({
                        'color': '17',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_17r !=0:
                count = item.color_17r
                while count !=0:
                    lst.append({
                        'color': '17R',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1

            if item.color_18 !=0:
                count = item.color_18
                while count !=0:
                    lst.append({
                        'color': '18',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1

            if item.color_19 !=0:
                count = item.color_19
                while count !=0:
                    lst.append({
                        'color': '19',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_20 !=0:
                count = item.color_20
                while count !=0:
                    lst.append({
                        'color': '20',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_21 !=0:
                count = item.color_21
                while count !=0:
                    lst.append({
                        'color': '21',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_22 !=0:
                count = item.color_22
                while count !=0:
                    lst.append({
                        'color': '22',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_23 !=0:
                count = item.color_23
                while count !=0:
                    lst.append({
                        'color': '23',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_24 !=0:
                count = item.color_24
                while count !=0:
                    lst.append({
                        'color': '24',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_25 !=0:
                count = item.color_25
                while count !=0:
                    lst.append({
                        'color': '25',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_26 !=0:
                count = item.color_26
                while count !=0:
                    lst.append({
                        'color': '26',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_27 !=0:
                count = item.color_27
                while count !=0:
                    lst.append({
                        'color': '27',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_28 !=0:
                count = item.color_28
                while count !=0:
                    lst.append({
                        'color': '28',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_29 !=0:
                count = item.color_29
                while count !=0:
                    lst.append({
                        'color': '29',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_30 !=0:
                count = item.color_30
                while count !=0:
                    lst.append({
                        'color': '30',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_31 !=0:
                count = item.color_31
                while count !=0:
                    lst.append({
                        'color': '31',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_32 !=0:
                count = item.color_32
                while count !=0:
                    lst.append({
                        'color': '32',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_33 !=0:
                count = item.color_33
                while count !=0:
                    lst.append({
                        'color': '33',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_34 !=0:
                count = item.color_34
                while count !=0:
                    lst.append({
                        'color': '34',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_35 !=0:
                count = item.color_35
                while count !=0:
                    lst.append({
                        'color': '35',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_36 !=0:
                count = item.color_36
                while count !=0:
                    lst.append({
                        'color': '36',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_37 !=0:
                count = item.color_37
                while count !=0:
                    lst.append({
                        'color': '37',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -=1
            if item.color_38 != 0:
                count = item.color_38
                while count != 0:
                    lst.append({
                        'color': '38',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                count -= 1
            if item.color_39 != 0:
                count = item.color_39
                while count != 0:
                    lst.append({
                        'color': '39',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_40 != 0:
                count = item.color_40
                while count != 0:
                    lst.append({
                        'color': '40',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_41 != 0:
                count = item.color_41
                while count != 0:
                    lst.append({
                        'color': '41',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_42 != 0:
                count = item.color_42
                while count != 0:
                    lst.append({
                        'color': '42',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_43 != 0:
                count = item.color_43
                while count != 0:
                    lst.append({
                        'color': '43',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_44 != 0:
                count = item.color_44
                while count != 0:
                    lst.append({
                        'color': '44',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_45 != 0:
                count = item.color_45
                while count != 0:
                    lst.append({
                        'color': '45',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_46 != 0:
                count = item.color_46
                while count != 0:
                    lst.append({
                        'color': '46',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_47 != 0:
                count = item.color_47
                while count != 0:
                    lst.append({
                        'color': '47',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_48 != 0:
                count = item.color_48
                while count != 0:
                    lst.append({
                        'color': '48',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_49 != 0:
                count = item.color_49
                while count != 0:
                    lst.append({
                        'color': '49',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_50 != 0:
                count = item.color_50
                while count != 0:
                    lst.append({
                        'color': '50',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_51 != 0:
                count = item.color_51
                while count != 0:
                    lst.append({
                        'color': '51',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_52 != 0:
                count = item.color_52
                while count != 0:
                    lst.append({
                        'color': '52',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_53 != 0:
                count = item.color_53
                while count != 0:
                    lst.append({
                        'color': '53',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_54 != 0:
                count = item.color_54
                while count != 0:
                    lst.append({
                        'color': '54',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_55 != 0:
                count = item.color_55
                while count != 0:
                    lst.append({
                        'color': '55',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_56 != 0:
                count = item.color_56
                while count != 0:
                    lst.append({
                        'color': '56',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_57 != 0:
                count = item.color_57
                while count != 0:
                    lst.append({
                        'color': '57',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_58 != 0:
                count = item.color_58
                while count != 0:
                    lst.append({
                        'color': '58',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_59 != 0:
                count = item.color_59
                while count != 0:
                    lst.append({
                        'color': '59',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_60 != 0:
                count = item.color_60
                while count != 0:
                    lst.append({
                        'color': '60',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_61 != 0:
                count = item.color_61
                while count != 0:
                    lst.append({
                        'color': '61',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_62 != 0:
                count = item.color_62
                while count != 0:
                    lst.append({
                        'color': '62',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_63 != 0:
                count = item.color_63
                while count != 0:
                    lst.append({
                        'color': '63',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_64 != 0:
                count = item.color_64
                while count != 0:
                    lst.append({
                        'color': '64',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_65 != 0:
                count = item.color_65
                while count != 0:
                    lst.append({
                        'color': '65',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_66 != 0:
                count = item.color_66
                while count != 0:
                    lst.append({
                        'color': '66',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_67 != 0:
                count = item.color_67
                while count != 0:
                    lst.append({
                        'color': '67',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_68 != 0:
                count = item.color_68
                while count != 0:
                    lst.append({
                        'color': '68',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_69 != 0:
                count = item.color_69
                while count != 0:
                    lst.append({
                        'color': '69',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_70 != 0:
                count = item.color_70
                while count != 0:
                    lst.append({
                        'color': '70',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_71 != 0:
                count = item.color_71
                while count != 0:
                    lst.append({
                        'color': '71',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_72 != 0:
                count = item.color_72
                while count != 0:
                    lst.append({
                        'color': '72',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_73 != 0:
                count = item.color_73
                while count != 0:
                    lst.append({
                        'color': '73',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_74 != 0:
                count = item.color_74
                while count != 0:
                    lst.append({
                        'color': '74',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_75 != 0:
                count = item.color_75
                while count != 0:
                    lst.append({
                        'color': '75',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_76 != 0:
                count = item.color_76
                while count != 0:
                    lst.append({
                        'color': '76',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_77 != 0:
                count = item.color_77
                while count != 0:
                    lst.append({
                        'color': '77',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_78 != 0:
                count = item.color_78
                while count != 0:
                    lst.append({
                        'color': '78',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_79 != 0:
                count = item.color_79
                while count != 0:
                    lst.append({
                        'color': '79',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_80 != 0:
                count = item.color_80
                while count != 0:
                    lst.append({
                        'color': '80',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_81 != 0:
                count = item.color_81
                while count != 0:
                    lst.append({
                        'color': '81',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_82 != 0:
                count = item.color_82
                while count != 0:
                    lst.append({
                        'color': '82',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_83 != 0:
                count = item.color_83
                while count != 0:
                    lst.append({
                        'color': '83',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_84 != 0:
                count = item.color_84
                while count != 0:
                    lst.append({
                        'color': '84',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_85 != 0:
                count = item.color_85
                while count != 0:
                    lst.append({
                        'color': '85',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_86 != 0:
                count = item.color_86
                while count != 0:
                    lst.append({
                        'color': '86',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_87 != 0:
                count = item.color_87
                while count != 0:
                    lst.append({
                        'color': '87',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_88 != 0:
                count = item.color_88
                while count != 0:
                    lst.append({
                        'color': '88',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_89 != 0:
                count = item.color_89
                while count != 0:
                    lst.append({
                        'color': '89',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_90 != 0:
                count = item.color_90
                while count != 0:
                    lst.append({
                        'color': '90',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_91 != 0:
                count = item.color_91
                while count != 0:
                    lst.append({
                        'color': '91',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_92 != 0:
                count = item.color_92
                while count != 0:
                    lst.append({
                        'color': '92',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_93 != 0:
                count = item.color_93
                while count != 0:
                    lst.append({
                        'color': '93',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_94 != 0:
                count = item.color_94
                while count != 0:
                    lst.append({
                        'color': '94',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1

            if item.color_95 != 0:
                count = item.color_95
                while count != 0:
                    lst.append({
                        'color': '95',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_96 != 0:
                count = item.color_96
                while count != 0:
                    lst.append({
                        'color': '96',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_91 != 0:
                count = item.color_91
                while count != 0:
                    lst.append({
                        'color': '91',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_92 != 0:
                count = item.color_92
                while count != 0:
                    lst.append({
                        'color': '92',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_93 != 0:
                count = item.color_93
                while count != 0:
                    lst.append({
                        'color': '93',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_94 != 0:
                count = item.color_94
                while count != 0:
                    lst.append({
                        'color': '94',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_95 != 0:
                count = item.color_95
                while count != 0:
                    lst.append({
                        'color': '95',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_96 != 0:
                count = item.color_96
                while count != 0:
                    lst.append({
                        'color': '96',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_97 != 0:
                count = item.color_97
                while count != 0:
                    lst.append({
                        'color': '97',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_98 != 0:
                count = item.color_98
                while count != 0:
                    lst.append({
                        'color': '98',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_99 != 0:
                count = item.color_99
                while count != 0:
                    lst.append({
                        'color': '99',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1
            if item.color_100 != 0:
                count = item.color_100
                while count != 0:
                    lst.append({
                        'color': '100',
                        'design_name': item.design_id.name,
                        'quality_id': item.quality_id.name,
                        'child_design': item.child_design_id.name if item.child_design_id else ' - '
                    })
                    count -= 1

        return {
            'data': lst,
            'customer': order.partner_id.name,
            'sub_customer': order.sub_customer,
            'number': order.name,
            'customer_note': order.customer_note,
        }






