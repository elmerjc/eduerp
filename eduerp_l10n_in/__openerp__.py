# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'Indian EduERP',
    'version': '2.4.0',
    'category': 'Openerp Education',
    "sequence": 3,
    'summary': 'Indian Localization of EduERP',
    'complexity': "easy",
    'description': """
        This module adds Indian flavor to EduERP_Core.

    """,
    'author': 'Tech Receptives',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_core'],
    'data': [
        'views/student_view.xml',
        'views/faculty_view.xml',
        'views/category_view.xml',
        'views/religion_view.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [
        'demo/op.category.csv',
        'demo/op.religion.csv',
        'demo/op.student.csv',
        'demo/op.faculty.csv'
    ],
    'images': [
        'static/description/indian_eduerp_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
