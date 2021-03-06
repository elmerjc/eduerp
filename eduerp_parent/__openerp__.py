# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Parent',
    'version': '2.4.0',
    'category': 'Education ERP System',
    "sequence": 3,
    'summary': 'Manage Parent',
    'complexity': "easy",
    'description': """
        This module provide parent management system over OpenERP
    """,
    'author': 'VSEP',
    'website': '',
    'depends': ['eduerp_core'],
    'data': [
        'security/op_parent_security.xml',
        'views/parent_view.xml',
        'parent_menu.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [
        'demo/res.users.csv',
        'demo/res.groups.csv',
        'demo/res.partner.csv',
        'demo/op.parent.csv',
    ],
    'images': [
        'static/description/eduerp_parent_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
