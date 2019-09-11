# -*- coding: utf-8 -*-
{
    'name': "Tacna - Openhealth",

    'summary': """
        - View and Access profiles for Tacna.
    """,

    'description': """
        - View and Access profiles for Tacna.
    """,

    'author': "My Company",

    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',


    # any module necessary for this one to work correctly
    #'depends': ['base'],
    'depends': ['base', 'openhealth', 'matrix'],


    # always loaded

    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',

        #'views/menus.xml',
        'views/actions.xml',
    ],



    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],

}