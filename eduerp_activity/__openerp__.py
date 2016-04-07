# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Activity',
    'version': '2.4.0',
    'category': 'Openerp Education',
    "sequence": 3,
    'summary': 'Manage Activities',
    'complexity': "easy",
    'description': """
        This module provide feature of Activity Manangement.

    """,
    'author': 'Tech Receptives',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_core'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/student_migrate_wizard_view.xml',
        'views/activity_view.xml',
        'views/activity_type_view.xml',
        'views/student_view.xml',
        'activity_menu.xml'
    ],
    'demo': [
        'demo/op.activity.type.csv',
        'demo/op.activity.csv',
    ],
    'images': [
        'static/description/eduerp_activity_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
