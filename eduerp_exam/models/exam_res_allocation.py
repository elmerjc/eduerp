# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api


class OpExamResAllocation(models.Model):
    _name = 'op.exam.res.allocation'

    exam_session_ids = fields.Many2many(
        'op.exam.session', string='Select Exam Session')
    exam_ids = fields.Many2many('op.exam', string='Exam(s)')
    faculty_ids = fields.Many2many('op.faculty', string='Faculty')
    student_ids = fields.Many2many('op.student', string='Student')

    @api.onchange('exam_session_ids')
    def onchange_exam_session_res(self):
        for session in self.exam_session_ids:
            students = self.env['op.student'].search(
                [('course_id', '=', session.course_id.id)])
            self.exam_ids = session.exam_ids.ids
            self.student_ids = students.ids

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
