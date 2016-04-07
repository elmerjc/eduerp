# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################

{
    'name': "Indian EduERP Admission",
    'version': '2.4.0',
    'category': 'Openerp Education',
    'sequence': 3,
    'summary': "Manage Indian Based Admission""",
    'complexity': "easy",
    'description': """
        This module provide indian based feature of admission.
    """,
    'author': 'Tech Receptives',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_l10n_in', 'eduerp_admission'],
    'data': [
        'views/admission_view.xml',
    ],
    'demo': [
        'demo/op.admission.csv'
    ],
    'images': [
        'static/description/indian_eduerp_admission_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
