# -*- coding: utf-8 -*-
{
    'name': "sale_order_list_changs",

    'summary': """
        This module is all about sale order list view changes and some other fields in form view""",

    'description': """
        this module will provide detail changes about sale order list view changes and some other field changes in form view
        
    """,

    'author': "SK Technology",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/sale_order_list_view_changes.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
