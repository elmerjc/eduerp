# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api


class StudentHallTicket(models.TransientModel):

    """ Student Hall Ticket Wizard """
    _name = 'student.hall.ticket'

    exam_session_id = fields.Many2one(
        'op.exam.session', 'Exam Session', required=True)

    @api.multi
    def print_report(self):
        data = self.read(['exam_session_id'])[0]
        return self.env['report'].get_action(
            self, 'eduerp_exam.report_ticket', data=data)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
