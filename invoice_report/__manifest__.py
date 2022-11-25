# -*- coding: utf-8 -*-
{
    'name': "invoice_report",

    'summary': """ This module is all about invoice report""",

    'description': """
        This module is all about invoicing detail
    """,

    'author': "SK Technology",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/report_action.xml',
        'report/report_template.xml',
        'report/invoice_report_header.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
