# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpFaculty(models.Model):

    _inherit = 'op.faculty'

    health_faculty_lines = fields.One2many(
        'op.health', 'faculty_id', 'Health Detail')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
