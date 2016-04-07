# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpStudent(models.Model):
    _inherit = 'op.student'

    activity_log = fields.One2many(
        'op.activity', 'student_id', 'Activity Log')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
