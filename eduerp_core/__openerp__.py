# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Core',
    'version': '2.4.0',
    'category': 'Education ERP System',
    "sequence": 1,
    'summary': 'Manage Students, Faculties and Education Institute',
    'complexity': "easy",
    'description': """
        This module provide core education management system over OpenERP
        Features includes managing
            * Student
            * Faculty
            * Course
            * Batch

    """,
    'author': 'VSEP',
    'website': '',
    'depends': ['board', 'document', 'hr', 'web', 'website'],
    'data': [
        'report/report_student_bonafide.xml',
        'report/report_student_idcard.xml',
        'report/report_menu.xml',
        'wizard/faculty_create_employee_wizard_view.xml',
        'wizard/faculty_create_user_wizard_view.xml',
        'wizard/students_create_user_wizard_view.xml',
        'security/op_security.xml',
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/hr_view.xml',
        'views/course_view.xml',
        'views/batch_view.xml',
        'views/subject_view.xml',
        'views/roll_number_view.xml',
        'views/faculty_view.xml',
        'views/res_company_view.xml',
        'views/eduerp_template.xml',
        'views/homepage_template.xml',
        'views/website_assets.xml',
        'dashboard/faculty_dashboard_view.xml',
        'dashboard/student_dashboard_view.xml',
        'menu/eduerp_core_menu.xml',
        'menu/faculty_menu.xml',
        'menu/student_menu.xml'
    ],
    'demo': [
        'demo/base_demo.xml',
        'demo/website_demo.xml',
        'demo/op.subject.csv',
        'demo/op.course.csv',
        'demo/op.batch.csv',
        'demo/res.users.csv',
        'demo/op.student.csv',
        'demo/op.faculty.csv',
        'demo/student_demo.xml',
        'demo/faculty_demo.xml',
        'demo/op.roll.number.csv',
        'demo/res.groups.csv'
    ],
    'css': ['static/src/css/base.css'],
    'qweb': [
        'static/src/xml/base.xml'],
    'js': ['static/src/js/chrome.js'],
    'images': [
        'static/description/eduerp_core_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
