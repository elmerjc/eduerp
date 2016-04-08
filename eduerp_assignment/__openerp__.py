# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Assignment',
    'version': '2.4.0',
    'category': 'Openerp Education',
    "sequence": 3,
    'summary': 'Manage Assgiments',
    'complexity': "easy",
    'description': """
        This module provide feature of Assignments.

    """,
    'author': 'VSEP',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_core'],
    'data': [
        'security/ir.model.access.csv',
        'views/assignment_view.xml',
        'views/assignment_type_view.xml',
        'views/assignment_sub_line_view.xml',
        'views/student_view.xml',
        'dashboard/assignment_faculty_dashboard.xml',
        'dashboard/assignment_student_dashboard.xml',
        'assignment_menu.xml'
    ],
    'demo': [
        'demo/op.assignment.type.csv',
        'demo/op.assignment.csv',
        'demo/op.assignment.sub.line.csv'
    ],
    'images': [
        'static/description/eduerp_assignment_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
