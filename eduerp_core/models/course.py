# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpCourse(models.Model):
    _name = 'op.course'

    name = fields.Char('Name', size=32, required=True)
    code = fields.Char('Code', size=8, required=True)
    parent_id = fields.Many2one('op.course', 'Parent Course')
    section = fields.Char('Section', size=32, required=True)
    evaluation_type = fields.Selection(
        [('normal', 'Normal'), ('GPA', 'GPA'), ('CWA', 'CWA'), ('CCE', 'CCE')],
        'Evaluation Type', default="normal", required=True)
    subject_ids = fields.Many2many('op.subject', string='Subject(s)')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
