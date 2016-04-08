# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

{
    'name': 'EduERP Facility',
    'version': '2.4.0',
    'category': 'Openerp Education',
    "sequence": 3,
    'summary': 'Manage Facility',
    'complexity': "easy",
    'description': """
        This module adds the feature of facility in Openeducat
    """,
    'author': 'VSEP',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_core'],
    'data': [
        'views/facility_view.xml',
        'views/facility_line_view.xml',
        'security/ir.model.access.csv',
        'facility_menu.xml',
    ],
    'demo': [
        'demo/op.facility.csv'
    ],
    'images': [
        'static/description/eduerp_facility_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
