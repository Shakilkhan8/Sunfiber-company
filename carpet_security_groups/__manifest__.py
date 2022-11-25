# -*- coding: utf-8 -*-
{
    'name': "carpet_security_groups",

    'summary': """Carpet modules security groups""",

    'description': """
    This module provide security about all all modules of carpet production
    """,

    'author': "SK Technology",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'stock','carpet_color', 'carpet_product_barcod', 'carpet_product_field'],

    'data': [
        'security/carpet_security_groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',

    ],

}
