# -*- coding: utf-8 -*-
{
    'name': "carpet_product_barcod",

    'summary': """this module is used to print product barcode for each product and at the same time to print the barcode""",

    'description': """
    This module is used to print the barcode for each product, the print label should 
    contain the combination product name and color
     
    """,

    'author': "SK Tecnology",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'carpet_product_field'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/carpet_product_barcode_view.xml',
        'report/barcode_action.xml',
        'report/barcode_lable.xml',
        'report/barcode_formate.xml',
        # 'report/report_formate.xml',
        # 'report/report_formate.xml',

    ],

'assets': {
        'web.assets_frontend': [
            # 'pos_address/static/src/js/yourjs.js',
            'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css',
            'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.7.5/css/bootstrap-select.min.css',
            'https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js',
            'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.7.5/js/bootstrap-select.min.js',
        ],
    },


    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
