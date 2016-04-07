# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Scholarship',
    'version': '2.4.0',
    'category': 'Openerp Education',
    "sequence": 3,
    'summary': 'Manage Scholarship',
    'complexity': "easy",
    'description': """
        This module adds the feature of scholarship in Openeducat
    """,
    'author': 'Tech Receptives',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_core'],
    'data': [
        'views/scholarship_view.xml',
        'views/scholarship_type_view.xml',
        'security/ir.model.access.csv',
        'scholarship_menu.xml',
    ],
    'demo': [
        'demo/op.scholarship.type.csv',
        'demo/op.scholarship.csv',
    ],
    'images': [
        'static/description/eduerp_scholarship_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
