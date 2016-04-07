# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class OpExamAttendees(models.Model):
    _name = 'op.exam.attendees'
    _rec_name = 'student_id'

    student_id = fields.Many2one('op.student', 'Student', required=True)
    status = fields.Selection(
        [('present', 'Present'), ('absent', 'Absent')],
        'Status', default="present", required=True)
    marks = fields.Float('Marks')
    note = fields.Text('Note')
    exam_id = fields.Many2one('op.exam', 'Exam', required=True)
    course_id = fields.Many2one('op.course', 'Course', readonly=True)
    batch_id = fields.Many2one('op.batch', 'Batch', readonly=True)

    @api.onchange('exam_id')
    def onchange_exam(self):
        self.course_id = self.exam_id.session_id.course_id
        self.batch_id = self.exam_id.session_id.batch_id
        self.student_id = False

    @api.constrains('marks')
    def _check_marks(self):
        if self.marks < 0.0:
            raise ValidationError("Enter proper marks!")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
