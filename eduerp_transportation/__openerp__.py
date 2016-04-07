# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Transportation',
    'version': '2.4.0',
    'category': 'Openerp Education',
    "sequence": 3,
    'summary': 'Manage Transportations',
    'complexity': "easy",
    'description': """
        This module provide feature of Transportations.

    """,
    'author': 'Tech Receptives',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_core'],
    'data': [
        'security/ir.model.access.csv',
        'views/stop_view.xml',
        'views/transportation_view.xml',
        'views/vehicle_view.xml',
        'transportation_menu.xml'
    ],
    'demo': [
        'demo/op.stop.csv',
        'demo/op.vehicle.csv',
        'demo/op.transportation.csv',
    ],
    'images': [
        'static/description/eduerp_transportation_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
