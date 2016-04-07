# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api


class ReturnDate(models.TransientModel):

    """ Assign return date """
    _name = 'return.date'

    actual_return_date = fields.Date(
        'Actual Return Date', required=True,
        default=lambda self: fields.Date.today())

    @api.one
    def assign_return_date(self):
        book_movement = self.env['op.book.movement'].browse(
            self.env.context.get('active_ids', False))
        book_movement.write(
            {'actual_return_date': self.actual_return_date})
        book_movement.calculate_penalty()
        book_movement.state = 'return'
        book_movement.book_unit_id.state = 'available'


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
