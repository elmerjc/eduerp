# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpFacility(models.Model):
    _name = 'op.facility'
    _rec_name = 'name'

    name = fields.Char('Name', size=16, required=True)
    code = fields.Char('Code', size=4, required=True)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
