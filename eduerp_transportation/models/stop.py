# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpStop(models.Model):
    _name = 'op.stop'
    _order = 'sequence asc'

    name = fields.Char('Name', size=64, required=True)
    sequence = fields.Integer('Sequence')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
