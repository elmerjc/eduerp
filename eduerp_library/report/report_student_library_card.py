# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

import time

from openerp import models
from openerp.report import report_sxw


class OpStudentLibraryCardReport(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context=None):
        super(OpStudentLibraryCardReport, self).__init__(
            cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
        })


class ReportLibraryIdcard(models.AbstractModel):
    _name = 'report.eduerp_library.report_student_library_card'
    _inherit = 'report.abstract_report'
    _template = 'eduerp_library.report_student_library_card'
    _wrapped_report_class = OpStudentLibraryCardReport


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
