# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpStudent(models.Model):

    _inherit = 'op.student'

    health_lines = fields.One2many('op.health', 'student_id', 'Health Detail')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
