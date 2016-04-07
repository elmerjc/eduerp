# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpActivity(models.Model):
    _name = 'op.activity'
    _rec_name = 'student_id'
    _inherit = 'mail.thread'

    student_id = fields.Many2one('op.student', 'Student', required=True)
    faculty_id = fields.Many2one('op.faculty', 'Faculty')
    type_id = fields.Many2one('op.activity.type', 'Activity Type')
    description = fields.Text('Description')
    date = fields.Date('Date', default=fields.Date.today())


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
