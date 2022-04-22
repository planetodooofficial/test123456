
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Account Default Management',
    'version': '1.1',
    'summary': 'Account',
    'sequence': 10,
    'description': """
Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com/page/billing',
    'images': [],
    'depends': ['base', 'account','analytic'],
    'data': [
        # 'views/account_journal_view.xml',
        'views/account_move_view.xml',
        'views/tds_rates_view.xml',
        'security/ir.model.access.csv',

    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
