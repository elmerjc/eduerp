# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpResultExamLine(models.Model):
    _name = 'op.result.exam.line'
    _description = 'Result Exam Line'
    _rec_name = "exam_id"

    result_id = fields.Many2one('op.result.template.line', 'Session Template')
    exam_id = fields.Many2one('op.exam', 'Exam')
    pass_marks = fields.Float(
        'Passing Marks', related='exam_id.min_marks', readonly=True)
    total_marks = fields.Float(
        'Total Marks', related='exam_id.total_marks', readonly=True)
    weightage = fields.Float('Weightage')
    result_lines = fields.One2many(
        'op.result.line', 'exam_tmpl_id', 'Result Lines')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
