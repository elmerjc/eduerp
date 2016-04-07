# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpReligion(models.Model):
    _name = 'op.religion'

    name = fields.Char('Name', size=256, required=True)
    code = fields.Char('Code', size=4, required=True)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
