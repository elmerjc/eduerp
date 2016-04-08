# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Health',
    'version': '2.4.0',
    'category': 'Education ERP System',
    "sequence": 3,
    'summary': 'Manage Health',
    'complexity': "easy",
    'description': """
        This module adds the feature of health in Openeducat
    """,
    'author': 'VSEP',
    'website': '',
    'depends': ['eduerp_core'],
    'data': [
        'views/health_view.xml',
        'security/ir.model.access.csv',
        'health_menu.xml',
    ],
    'demo': [
        'demo/op.health.line.csv',
        'demo/op.health.csv'
    ],
    'images': [
        'static/description/eduerp_health_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
