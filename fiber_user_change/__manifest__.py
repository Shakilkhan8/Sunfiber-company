# -*- coding: utf-8 -*-
{
    'name': "Fiber User Changes",

    'summary': """This module is all about user changes""",

    'description': """
    In this module we add an extra field 'check_company' to see which company if active and which is not
    to do different calculation in sale order on the base of company 
    """,

    'author': "SK Technology",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

}
