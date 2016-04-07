# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api


class OpScholarship(models.Model):
    _name = 'op.scholarship'
    _inherit = 'mail.thread'
    _description = 'Scholarship'

    name = fields.Char('Name', size=64, required=True)
    student_id = fields.Many2one('op.student', 'Student', required=True)
    type_id = fields.Many2one('op.scholarship.type', 'Type', required=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('confirm', 'Confirm'),
         ('reject', 'Reject')], 'State', default='draft', readonly=True,
        select=True, track_visibility='onchange')

    @api.one
    def act_confirm(self):
        self.state = 'confirm'

    @api.one
    def act_reject(self):
        self.state = 'reject'


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
