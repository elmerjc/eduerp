# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class OpBookQueue(models.Model):
    _name = 'op.book.queue'
    _inherit = 'mail.thread'
    _rec_name = 'user_id'
    _description = 'Book Queue Request'

    name = fields.Char("Sequence No", readonly=True, copy=False, default='/')
    partner_id = fields.Many2one('res.partner', 'Student/Faculty')
    book_id = fields.Many2one(
        'op.book', 'Book', required=True, track_visibility='onchange')
    date_from = fields.Date(
        'From Date', required=True, default=fields.Date.today())
    date_to = fields.Date('To Date', required=True)
    user_id = fields.Many2one(
        'res.users', 'User', readonly=True, default=lambda self: self.env.uid)
    state = fields.Selection(
        [('request', 'Request'), ('accept', 'Accepted'),
         ('reject', 'Rejected')],
        'Status', copy=False, default='request', track_visibility='onchange')

    @api.onchange('user_id')
    def onchange_user(self):
        self.partner_id = self.user_id.partner_id.id

    @api.constrains('date_from', 'date_to')
    def _check_date(self):
        if self.date_from > self.date_to:
            raise ValidationError('To Date cannot be set before From Date.')

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'op.book.queue') or '/'
        return super(OpBookQueue, self).create(vals)

    @api.one
    def do_reject(self):
        self.state = 'reject'

    @api.one
    def do_accept(self):
        self.state = 'accept'

    @api.one
    def do_request_again(self):
        self.state = 'request'


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
