# -*- coding: utf-8 -*-
{
    'name': "Fiber Sale Order",

    'summary': """This module is used for fiber sale order mdification""",

    'description': """
    In this module we modify sale order for fiber company with different field in order line 
    """,

    'author': "SK TEchnology",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'sale_management','carpet_security_groups'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

}
