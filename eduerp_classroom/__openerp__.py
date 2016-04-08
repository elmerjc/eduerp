# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Classroom',
    'version': '2.4.0',
    'category': 'Openerp Education',
    "sequence": 3,
    'summary': 'Manage Classroom',
    'complexity': "easy",
    'description': """
        This module adds classroom management feature to EduERP_Core.
    """,
    'author': 'VSEP',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_core', 'eduerp_facility', 'product'],
    'data': [
        'views/classroom_view.xml',
        'classroom_menu.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [
        'demo/op.classroom.csv',
        'demo/op.facility.line.csv'
    ],
    'images': [
        'static/description/eduerp_classroom_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
