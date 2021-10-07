# -*- coding: utf-8 -*-
{
    'name': "Theme Elnoman",
    'web developer': "Ayah ashraf",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Sahara",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Theme',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','crm','website_form'],

    # always loaded
    'data': [
       'security/ir.model.access.csv',
        'views/assets.xml',
        'views/snippets_template.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/customer_review.xml',
        'views/product_template.xml',
        'data/pages.xml',
    ],
    'images': [
        # 'static/description/banner.png',
        'static/src/description/banner_screenshot.png',
    ],
}
