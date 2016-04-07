# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################

{
    'name': "EduERP Admission",
    'version': '2.4.0',
    'category': 'Openerp Education',
    'sequence': 3,
    'summary': "Manage Admissions""",
    'complexity': "easy",
    'description': """
        This is gives the feature of admission process.
    """,
    'author': 'Tech Receptives',
    'website': 'http://www.eduerp.org',
    'depends': ['eduerp_fees'],
    'data': [
        'views/admission_register_view.xml',
        'views/admission_view.xml',
        'views/admission_sequence.xml',
        'report/report_menu.xml',
        'report/report_admission_analysis.xml',
        'wizard/admission_analysis_wizard_view.xml',
        'admission_menu.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/product.category.csv',
        'demo/product.product.csv',
        'demo/op.admission.register.csv',
        'demo/op.admission.csv',
        'demo/student_demo.xml',
    ],
    'images': [
        'static/description/eduerp_admission_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
