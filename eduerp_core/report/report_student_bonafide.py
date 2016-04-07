# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

import time
from openerp import models
from openerp.report import report_sxw


class StudentBonafideCertificate(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context=None):
        super(StudentBonafideCertificate, self).__init__(
            cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
        })


class ReportStudentBonafide(models.AbstractModel):
    _name = 'report.eduerp_core.report_student_bonafide'
    _inherit = 'report.abstract_report'
    _template = 'eduerp_core.report_student_bonafide'
    _wrapped_report_class = StudentBonafideCertificate


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
