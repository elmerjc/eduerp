# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Achievement',
    'version': '2.4.0',
    'category': 'Education ERP System',
    "sequence": 3,
    'summary': 'Manage Achievement',
    'complexity': "easy",
    'description': """
        This module adds the feature of achievement in Openeducat
    """,
    'author': 'VSEP',
    'website': '',
    'depends': ['eduerp_core'],
    'data': [
        'views/achievement_view.xml',
        'views/achievement_type_view.xml',
        'security/ir.model.access.csv',
        'achievement_menu.xml',
    ],
    'images': [
        'static/description/eduerp_achievement_banner.jpg',
    ],
    'demo': [
        'demo/op.achievement.type.csv',
        'demo/op.achievement.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
