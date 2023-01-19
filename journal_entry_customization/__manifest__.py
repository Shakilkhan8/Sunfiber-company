# -*- coding: utf-8 -*-
{
    'name': "Journal Entry Customization",

    'summary': """This module is all about journal entry customization""",

    'description': """
       This module is all about journal entry customization
    """,

    'author': "SK Technology",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

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
