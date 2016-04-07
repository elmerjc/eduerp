# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpAuthor(models.Model):
    _name = 'op.author'

    name = fields.Char('Name', size=128, required=True)
    address = fields.Many2one('res.partner', 'Address')
    book_ids = fields.Many2many('op.book', string='Book(s)')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
