# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Hostel',
    'version': '2.4.0',
    'category': 'Education ERP System',
    "sequence": 3,
    'summary': 'Manage Hostels',
    'complexity': "easy",
    'description': """
        This module adds hostel management feature to EduERP_Core.
    """,
    'author': 'VSEP',
    'website': '',
    'depends': ['eduerp_core', 'eduerp_facility'],
    'data': [
        'views/room_view.xml',
        'views/hostel_view.xml',
        'views/hostel_room_view.xml',
        'hostel_menu.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/op.hostel.csv',
        'demo/op.room.csv',
        'demo/op.hostel.room.csv',
    ],
    'images': [
        'static/description/eduerp_hostel_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
