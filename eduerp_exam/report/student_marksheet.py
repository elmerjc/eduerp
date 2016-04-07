# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from datetime import datetime
import time

from openerp import models
from openerp.report import report_sxw


class MarksheetReport(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context=None):
        super(MarksheetReport, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'get_objects': self.get_objects,
            'get_lines': self.get_lines,
            'get_date': self.get_date,
            'get_total': self.get_total
        })

    def get_objects(self, objects):
        obj = []
        for object in objects:
            obj.extend(object)
        return obj

    def get_lines(self, obj):
        lines = []
        for line in obj.marksheet_line:
            lines.extend(line)
        return lines

    def get_date(self, date):
        date1 = datetime.strptime(date, "%Y-%m-%d")
        return str(date1.month) + ' / ' + str(date1.year)

    def get_total(self, marksheet_line):
        total = [x.total_marks for x in marksheet_line.result_line]
        return sum(total)


class ReportMarksheetReport(models.AbstractModel):
    _name = 'report.eduerp_exam.report_marksheet_report'
    _inherit = 'report.abstract_report'
    _template = 'eduerp_exam.report_marksheet_report'
    _wrapped_report_class = MarksheetReport


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
