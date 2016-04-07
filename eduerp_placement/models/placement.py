# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api


class OpPlacementOffer(models.Model):
    _name = 'op.placement.offer'
    _inherit = 'mail.thread'
    _description = 'Placement Offer'

    name = fields.Char('Company Name', required=True)
    student_id = fields.Many2one('op.student', 'Student Name', required=True)
    join_date = fields.Date('Join Date', default=fields.Date.today())
    offer_package = fields.Char('Offered Package', size=256)
    training_period = fields.Char('Training Period', size=256)
    state = fields.Selection(
        [('draft', 'Draft'), ('offer', 'Offer'), ('join', 'Join'),
         ('reject', 'Rejected'), ('cancel', 'Cancel')], 'State',
        default='draft', track_visibility='onchange')

    @api.one
    def placement_offer(self):
        self.state = 'offer'

    @api.one
    def placement_join(self):
        self.state = 'join'

    @api.one
    def confirm_rejected(self):
        self.state = 'reject'

    @api.one
    def confirm_to_draft(self):
        self.state = 'draft'

    @api.one
    def confirm_cancel(self):
        self.state = 'cancel'


class OpStudent(models.Model):

    _inherit = 'op.student'

    placement_line = fields.One2many(
        'op.placement.offer', 'student_id', 'Placement Details')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
