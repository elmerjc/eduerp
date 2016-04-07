# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Exam',
    'version': '2.4.0',
    'category': 'Openerp Education',
    "sequence": 3,
    'summary': 'Manage Exam',
    'complexity': "easy",
    'description': """
        This module provide exam management system over OpenERP
    """,
    'author': 'Tech Receptives',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_classroom'],
    'data': [
        'views/exam_attendees_view.xml',
        'views/exam_res_allocation_view.xml',
        'views/exam_room_view.xml',
        'views/exam_session_view.xml',
        'views/exam_type_view.xml',
        'views/exam_view.xml',
        'views/marksheet_line_view.xml',
        'views/marksheet_register_view.xml',
        'views/min_clearance_criteria_view.xml',
        'views/pass_status_view.xml',
        'views/result_exam_line_view.xml',
        'views/result_line_view.xml',
        'views/result_template_line_view.xml',
        'views/result_template_view.xml',
        'report/report_ticket.xml',
        'report/student_marksheet.xml',
        'report/report_exam_student_label.xml',
        'report/report_menu.xml',
        'wizard/student_hall_tickets_wizard_view.xml',
        'security/ir.model.access.csv',
        'exam_menu.xml',
    ],
    'demo': [
        'demo/op.classroom.csv',
        'demo/op.exam.room.csv',
        'demo/op.exam.type.csv',
        'demo/op.exam.session.csv',
        'demo/op.exam.csv',
        'demo/op.exam.attendees.csv'
    ],
    'images': [
        'static/description/eduerp_exam_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
