# -*- coding: utf-8 -*-
{
    'name': "carpet_product_field",

    'summary': """ in this module we inherit product template and add some fields for carpet corporation requirements""",

    'description': """
    in this module we also add some other custom model for quality and grade of the carpet for product to compherensively define the product tempalte
    """,

    'author': "SK Technology",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock' ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/carpet_product_fields_view.xml',
        'views/carpet_product_quality.xml',
        'views/carpet_grades.xml',
        'views/product_category_changes_view.xml',
        'views/product_template_search_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
