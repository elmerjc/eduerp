# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api


class OpAttendanceRegister(models.Model):
    _name = 'op.attendance.register'

    name = fields.Char('Name', size=16, required=True)
    code = fields.Char('Code', size=8, required=True)
    course_id = fields.Many2one('op.course', 'Course', required=True)
    batch_id = fields.Many2one('op.batch', 'Batch', required=True)
    subject_id = fields.Many2one('op.subject', 'Subject')

    @api.onchange('course_id')
    def onchange_course(self):
        self.batch_id = False


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
