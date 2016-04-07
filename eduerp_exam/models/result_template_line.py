# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api


class OpResultTemplateLine(models.Model):
    _name = 'op.result.template.line'
    _rec_name = 'exam_session_id'
    _description = 'Result Template Line'

    exam_session_id = fields.Many2one('op.exam.session', 'Exam Session')
    detailed_report = fields.Boolean('Detailed Report')
    course_id = fields.Many2one(
        'op.course', 'Course', related='exam_session_id.course_id',
        readonly=True)
    batch_id = fields.Many2one(
        'op.batch', 'Batch', related='exam_session_id.batch_id', readonly=True)
    result_id = fields.Many2one('op.result.template', 'Result Template Line')
    exam_lines = fields.One2many(
        'op.result.exam.line', 'result_id', 'Exam Lines')

    @api.onchange('exam_session_id')
    def onchange_exam_session(self):
        for exam_obj in self.exam_session_id.exam_ids:
            self.exam_lines += self.exam_lines.create(
                {'exam_id': exam_obj.id, 'weightage': 100})


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
