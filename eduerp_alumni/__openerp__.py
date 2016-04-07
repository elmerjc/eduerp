# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Alumni',
    'version': '2.4.0',
    'category': 'Openerp Education',
    "sequence": 3,
    'summary': 'Manage Alumni',
    'complexity': "easy",
    'description': """
        This module provide alumni management system over OpenERP
    """,
    'author': 'Tech Receptives',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_core'],
    'data': [
        'views/alumni_view.xml'
    ],
    'demo': [
        'demo/op.student.csv',
        'demo/op.roll.number.csv',
        'demo/student_demo.xml'
    ],
    'images': [
        'static/description/eduerp_alumni_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
