# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

import time
from openerp import models, fields, api
from openerp.exceptions import ValidationError


class AdmissionAnalysis(models.TransientModel):

    """ Admission Analysis Wizard """
    _name = 'admission.analysis'

    course_id = fields.Many2one('op.course', 'Course', required=True)
    start_date = fields.Date(
        'Start Date', default=time.strftime('%Y-%m-01'), required=True)
    end_date = fields.Date('End Date', required=True)

    @api.multi
    def print_report(self):
        start_date = fields.Date.from_string(self.start_date)
        end_date = fields.Date.from_string(self.end_date)
        if start_date > end_date:
            raise ValidationError("End Date cannot be set before Start Date.")
        else:
            data = self.read(
                ['course_id', 'start_date', 'end_date'])[0]
            return self.env['report'].get_action(
                self, 'eduerp_admission.report_admission_analysis',
                data=data)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
