# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

import time
from openerp import models
from openerp.report import report_sxw


class OpStudentIdcardReport(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context=None):
        super(OpStudentIdcardReport, self).__init__(
            cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
        })


class ReportStudentIdcard(models.AbstractModel):
    _name = 'report.eduerp_core.report_student_idcard'
    _inherit = 'report.abstract_report'
    _template = 'eduerp_core.report_student_idcard'
    _wrapped_report_class = OpStudentIdcardReport


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
