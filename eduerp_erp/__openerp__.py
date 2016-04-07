# -*- coding: utf-8 -*-
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'EduERP ERP',
    'version': '2.4.0',
    'category': 'Openerp Education',
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
    'author': 'Tech Receptives',
    'website': 'http://www.eduerp.org',
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
