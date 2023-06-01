# -*- coding: utf-8 -*-
{
    'name': "Vinculate Invoice Sale - Purchase",

    'summary': """
        Vinculate Invoice Sale - Purchase
        """,


    'description': """
        Vinculate Invoice Sale - Purchase
    """,

    'author': "JZolutions",
    'website': "https://www.linkedin.com/in/jesus-sanchez-jibaja-03a59ab7/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'price': 50.00,
    'currency': 'USD',

    # any module necessary for this one to work correctly
    'depends': ['purchase','sale'],

    # always loaded
    'data': [
        'views/group.xml',
        'views/sale_order.xml',
        'views/account_move.xml',

    ],


}
