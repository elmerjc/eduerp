# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpFaculty(models.Model):
    _inherit = 'op.faculty'

    timetable_ids = fields.One2many('op.timetable', 'faculty_id', 'TimeTables')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
