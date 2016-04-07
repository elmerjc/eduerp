# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpAttendanceLine(models.Model):
    _name = 'op.attendance.line'
    _rec_name = 'attendance_id'

    attendance_id = fields.Many2one(
        'op.attendance.sheet', 'Attendance Sheet', required=True)
    student_id = fields.Many2one('op.student', 'Student', required=True)
    present = fields.Boolean('Present ?', default=True)
    course_id = fields.Many2one(
        'op.course', 'Course',
        related='attendance_id.register_id.course_id', store=True,
        readonly=True)
    batch_id = fields.Many2one(
        'op.batch', 'Batch',
        related='attendance_id.register_id.batch_id', store=True,
        readonly=True)
    remark = fields.Char('Remark', size=256)
    attendance_date = fields.Date(
        'Date', related='attendance_id.attendance_date', store=True,
        readonly=True)

    _sql_constraints = [
        ('unique_student',
         'unique(student_id,attendance_id,attendance_date)',
         'Student must be unique per Attendance.'),
    ]


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
