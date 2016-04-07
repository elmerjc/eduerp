# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields

unit_states = [('available', 'Available'), ('issue', 'Issued'),
               ('reserve', 'Reserved'), ('lost', 'Lost')]


class OpBookUnit(models.Model):
    _name = 'op.book.unit'
    _inherit = 'mail.thread'
    _description = 'Book Unit'

    name = fields.Char('Name', required=True)
    book_id = fields.Many2one(
        'op.book', 'Book', required=True, track_visibility='onchange')
    barcode = fields.Char('Barcode', size=20)
    movement_lines = fields.One2many(
        'op.book.movement', 'book_unit_id', 'Movements')
    state = fields.Selection(
        unit_states, 'State', default='available', track_visibility='onchange')

    _sql_constraints = [
        ('unique_name_barcode',
         'unique(barcode)',
         'Barcode must be unique per book unit!'),
    ]


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
