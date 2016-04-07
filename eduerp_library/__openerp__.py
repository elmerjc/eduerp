# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Library',
    'version': '2.4.0',
    'category': 'Openerp Education',
    "sequence": 3,
    'summary': 'Manage Library',
    'complexity': "easy",
    'description': """
        This module provide feature of Library Management.

    """,
    'author': 'Tech Receptives',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_core'],
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'report/report_book_barcode.xml',
        'report/report_student_library_card.xml',
        'report/report_menu.xml',
        'wizards/issue_book_view.xml',
        'wizards/return_book_view.xml',
        'wizards/returndate_view.xml',
        'wizards/reserve_book_view.xml',
        'views/book_view.xml',
        'views/book_unit_view.xml',
        'views/book_movement_view.xml',
        'views/book_purchase_view.xml',
        'views/book_queue_view.xml',
        'views/library_view.xml',
        'views/author_view.xml',
        'views/publisher_view.xml',
        'views/tag_view.xml',
        'views/student_view.xml',
        'views/faculty_view.xml',
        'book_queue_sequence.xml',
        'dashboard/librarian_dashboard_view.xml',
        'menus/library_menu.xml',
    ],
    'demo': [
        'demo/res.users.csv',
        'demo/res.groups.csv',
        'demo/op.tag.csv',
        'demo/op.publisher.csv',
        'demo/op.author.csv',
        'demo/op.book.csv',
        'demo/op.book.unit.csv',
        'demo/op.book.queue.csv',
    ],
    'images': [
        'static/description/eduerp_library_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
