# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpStudent(models.Model):
    _inherit = 'op.student'

    library_card_id = fields.Many2one('op.library.card', 'Library Card')
    book_movement_lines = fields.One2many(
        'op.book.movement', 'student_id', 'Movements')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
