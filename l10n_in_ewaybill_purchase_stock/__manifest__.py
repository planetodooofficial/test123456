# -*- coding: utf-8 -*-
{
    'name': "eWayBill for India (Purchase-Stock)",

    'summary': """
        Create an eWayBill to transer the goods in India""",

    'description': """
        This module link Purchase bill and stock picking to get bill and ship address
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting/Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["stock", "purchase", "l10n_in_ewaybill", "l10n_in_ewaybill_stock"],

    "installable": True,
    "auto_install": True,
    'license': 'OEEL-1',
}
