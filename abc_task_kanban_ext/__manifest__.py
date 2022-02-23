# -*- coding: utf-8 -*-
{
    'name': "abc_task_kanban_ext",

    'summary': """
        Rende visibile sulla vista Kanban il campo Data scadenza sui task completati e la prossima ricorrenza""",

    'description': """
        Rende visibile sulla vista Kanban il campo Data scadenza sui task completati e la prossima ricorrenza
    """,

    'author': "Massimo Masi",
    'website': "https://www.abcstategie.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/kanban_ext.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
