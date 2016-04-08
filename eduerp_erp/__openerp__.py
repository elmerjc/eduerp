# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################

{
    'name': 'EduERP ERP',
    'version': '2.4.0',
    'category': 'Education ERP System',
    "sequence": 3,
    'summary': 'Manage Students, Faculties and Education Institute',
    'complexity': "easy",
    'description': """
        This module provide overall education management system overOpenERP
        Features includes managing
            * Student
            * Faculty
            * Admission
            * Course
            * Batch
            * Standard
            * Books
            * Library
            * Lectures
            * Exams
            * Marksheet
            * Result
            * Transportation
            * Hostel

    """,
    'author': 'VSEP',
    'website': '',
    'depends': ['eduerp_achievement', 'eduerp_activity',
                'eduerp_alumni', 'eduerp_assignment',
                'eduerp_attendance', 'eduerp_exam',
                'eduerp_health', 'eduerp_hostel',
                'eduerp_admission', 'eduerp_library',
                'eduerp_parent', 'eduerp_placement',
                'eduerp_scholarship', 'eduerp_timetable',
                'eduerp_transportation'],
    'data': [
    ],
    'demo': [
    ],
    'images': [
        'static/description/eduerp_erp_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
