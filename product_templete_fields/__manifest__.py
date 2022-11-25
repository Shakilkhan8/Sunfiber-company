# -*- coding: utf-8 -*-
{
    'name': "product_templete_fields",

    'summary': """ This module is all about product template fields where
     we add some fields which are used for carpet production""",

    'description': """
    in this module we added some fields in product template tree view , the fields are length, width, color and quality
    """,

    'author': "SK Technology",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product_template_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
