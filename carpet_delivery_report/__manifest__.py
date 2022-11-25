# -*- coding: utf-8 -*-
{
    'name': "carpet_delivery_report",

    'summary': """
        This module is all about delivery report""",

    'description': """
    In this module we print the report of the delivery where we calculate
     product total length , and total quantity of the product present in the invoice line
    """,

    'author': "SK Technology",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'Report/report.xml',
        'Report/template.xml',
        'Report/report_formate.xml',
        'Report/packing_list_header.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
