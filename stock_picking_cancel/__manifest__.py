# -*- coding: utf-8 -*-
{
    'name': "Force Stock Picking Cancel",

    'depends': ['base','stock','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/stock_picking.xml',
        'views/sale_order.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
