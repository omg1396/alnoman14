# -*- coding: utf-8 -*-
{
    'name': "Check Header Footer,Add Payment name,Signture",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','account','sale','purchase'],

    # always loaded
    'data': [
        'reports/payment_format.xml',
        'reports/payment_custom_report.xml',
        'reports/payment_report_inherit.xml',
        'reports/footer.xml',


    ],
}
