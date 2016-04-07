# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class OpExamSession(models.Model):
    _name = 'op.exam.session'
    _description = 'Exam Session'

    name = fields.Char('Exam', size=256, required=True)
    course_id = fields.Many2one('op.course', 'Course', required=True)
    batch_id = fields.Many2one('op.batch', 'Batch', required=True)
    exam_code = fields.Char('Exam Code', size=8, required=True)
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    room_id = fields.Many2one('op.exam.room', 'Room', required=True)
    exam_ids = fields.One2many('op.exam', 'session_id', 'Exam(s)')

    @api.constrains('start_date', 'end_date')
    def _check_date_time(self):
        if self.start_date > self.end_date:
            raise ValidationError(
                'End Date cannot be set before Start Date.')

    @api.onchange('course_id')
    def onchange_course(self):
        self.batch_id = False


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
