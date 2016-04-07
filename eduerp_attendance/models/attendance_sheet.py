# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api


class OpAttendanceSheet(models.Model):
    _name = 'op.attendance.sheet'

    @api.one
    @api.depends('attendance_line.present')
    def _total_present(self):
        self.total_present = len(self.attendance_line.filtered(
            lambda self: self.present))

    @api.one
    @api.depends('attendance_line.present')
    def _total_absent(self):
        self.total_absent = len(self.attendance_line.filtered(
            lambda self: self.present is False))

    name = fields.Char('Name', required=True, size=32)
    register_id = fields.Many2one(
        'op.attendance.register', 'Register', required=True)
    course_id = fields.Many2one(
        'op.course', related='register_id.course_id', store=True,
        readonly=True)
    batch_id = fields.Many2one(
        'op.batch', 'Batch', related='register_id.batch_id', store=True,
        readonly=True)
    attendance_date = fields.Date(
        'Date', required=True, default=lambda self: fields.Date.today())
    attendance_line = fields.One2many(
        'op.attendance.line', 'attendance_id', 'Attendance Line')
    total_present = fields.Integer(
        'Total Present', compute='_total_present')
    total_absent = fields.Integer(
        'Total Absent', compute='_total_absent')
    faculty_id = fields.Many2one('op.faculty', 'Faculty')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
