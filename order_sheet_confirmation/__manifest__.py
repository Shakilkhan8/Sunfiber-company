# -*- coding: utf-8 -*-
{
    'name': "order_sheet_confirmation",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'reports/order_report_format.xml',
        'reports/report_template.xml',
        'reports/report.xml',
        'reports/order_booking_with_price.xml',
        'reports/manual_packing_list_report.xml',
        'reports/manual_report_format.xml',
        'reports/report_header.xml',
        'reports/report_header_with_price.xml',
        'reports/order_report_formate_with_price.xml',
        'views/templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
