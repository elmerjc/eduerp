# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpMinClearanceCriteria(models.Model):
    _name = "op.min.clear.criteria"

    name = fields.Char('Name', size=256)
    number = fields.Float('Number of Failed Subject')
    result = fields.Char('Result to Display')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
