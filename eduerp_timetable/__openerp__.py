# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Timetable',
    'version': '2.4.0',
    'category': 'Openerp Education',
    "sequence": 3,
    'summary': 'Manage TimeTables',
    'complexity': "easy",
    'description': """
        This module provide feature of Timetable.

    """,
    'author': 'Tech Receptives',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_core'],
    'data': [
        'views/timetable_view.xml',
        'views/period_view.xml',
        'views/faculty_view.xml',
        'report/report_timetable_student_generate.xml',
        'report/report_timetable_teacher_generate.xml',
        'report/report_menu.xml',
        'wizard/generate_timetable_view.xml',
        'wizard/time_table_report.xml',
        'dashboard/timetable_student_dashboard.xml',
        'dashboard/timetable_faculty_dashboard.xml',
        'security/ir.model.access.csv',
        'timetable_menu.xml',
    ],
    'demo': [
        'demo/op.period.csv',
        'demo/op_timetable_demo.xml'
    ],
    'images': [
        'static/description/eduerp_timetable_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
