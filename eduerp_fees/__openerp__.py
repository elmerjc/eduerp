# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Fees',
    'version': '2.4.0',
    'category': 'Education ERP System',
    "sequence": 3,
    'summary': 'Manage Fees',
    'complexity': "easy",
    'description': """
        This module provide feature of fees collection &
        other finance operations.

    """,
    'author': 'VSEP',
    'website': '',
    'depends': ['eduerp_core', 'account_accountant'],
    'data': [
        'views/student_view.xml',
        'views/course_view.xml',
        'security/ir.model.access.csv'
    ],
    'images': [
        'static/description/eduerp_fees_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
