# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Attendance',
    'version': '2.4.0',
    'category': 'Openerp Education',
    "sequence": 3,
    'summary': 'Manage Attendances',
    'complexity': "easy",
    'description': """
        This module provide feature of Attendance Management.

    """,
    'author': 'Tech Receptives',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_core'],
    'data': [
        'security/ir.model.access.csv',
        'views/attendance_register_view.xml',
        'views/attendance_sheet_view.xml',
        'views/attendance_line_view.xml',
        'wizards/attendance_import_view.xml',
        'wizards/student_attendance_wizard_view.xml',
        'report/student_attendance_report.xml',
        'report/report_menu.xml',
        'attendance_menu.xml'
    ],
    'demo': [
        'demo/op.attendance.register.csv',
        'demo/op.attendance.sheet.csv',
        'demo/op.attendance.line.csv',
    ],
    'images': [
        'static/description/eduerp_attendance_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
