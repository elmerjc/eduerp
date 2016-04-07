# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Placement',
    'version': '2.4.0',
    'category': 'Openerp Education',
    "sequence": 3,
    'summary': 'Manage Placement',
    'complexity': "easy",
    'description': """
        This module provide placement management system over OpenERP
    """,
    'author': 'Tech Receptives',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_core'],
    'data': [
        'views/placement_view.xml',
        'placement_menu.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [
        'demo/op.placement.offer.csv'
    ],
    'images': [
        'static/description/eduerp_placement_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
