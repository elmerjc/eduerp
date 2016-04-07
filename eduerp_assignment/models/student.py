# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpStudent(models.Model):
    _inherit = 'op.student'

    allocation_ids = fields.Many2many('op.assignment', string='Assignment(s)')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
