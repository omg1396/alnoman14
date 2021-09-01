# -*- coding: utf-8 -*-
{
    'name': "Force Stock Picking Cancel",

    'depends': ['base','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/stock_picking.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
