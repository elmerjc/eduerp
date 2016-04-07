# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api


class OpAssignmentSubLine(models.Model):
    _name = 'op.assignment.sub.line'
    _inherit = 'mail.thread'
    _rec_name = 'assignment_id'
    _description = 'Assignment Submission'

    assignment_id = fields.Many2one(
        'op.assignment', 'Assignment', required=True)
    student_id = fields.Many2one(
        'op.student', 'Student',
        default=lambda self: self.env['op.student'].search(
            [('user_id', '=', self.env.uid)]), required=True)
    description = fields.Text('Description', track_visibility='onchange')
    state = fields.Selection(
        [('draft', 'Draft'), ('submit', 'Submitted'), ('reject', 'Rejected'),
         ('change', 'Change Req.'), ('accept', 'Accepted')], 'State',
        default='draft', track_visibility='onchange')
    submission_date = fields.Datetime(
        'Submission Date', readonly=True,
        default=lambda self: fields.Datetime.now(), required=True)
    note = fields.Text('Note')

    @api.one
    def act_draft(self):
        self.state = 'draft'

    @api.one
    def act_submit(self):
        self.state = 'submit'

    @api.one
    def act_accept(self):
        self.state = 'accept'

    @api.one
    def act_change_req(self):
        self.state = 'change'

    @api.one
    def act_reject(self):
        self.state = 'reject'


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
