# -*- coding: utf-8 -*-
{
    'name': "batch_number_update",

    'summary': """Updating batch number""",

    'description': """
        Updating batch number
    """,

    'author': "SK Technology",
    'website': "http://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
