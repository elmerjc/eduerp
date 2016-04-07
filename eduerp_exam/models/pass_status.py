# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpPassStatus(models.Model):
    _name = 'op.pass.status'
    _description = 'Pass Status'

    name = fields.Char('Name', size=256)
    number = fields.Float('Minimum Percentage')
    result = fields.Char('Result to Display')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
