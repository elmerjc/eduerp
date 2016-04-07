# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpPublisher(models.Model):
    _name = 'op.publisher'

    name = fields.Char('Name', size=20, required=True)
    address_id = fields.Many2one('res.partner', 'Address')
    book_ids = fields.Many2many('op.book', string='Book(s)')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
