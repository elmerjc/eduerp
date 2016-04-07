# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpTag(models.Model):
    _name = 'op.tag'

    name = fields.Char('Name', size=64, required=True)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
