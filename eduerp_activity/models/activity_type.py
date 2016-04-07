# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpActivityType(models.Model):
    _name = 'op.activity.type'

    name = fields.Char('Name', size=128, required=True)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
