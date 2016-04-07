# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpAlumni(models.Model):

    _inherit = 'op.student'

    alumni_boolean = fields.Boolean('Alumni Student')
    passing_year = fields.Many2one('op.batch', 'Passing Year')
    current_position = fields.Char('Current Position', size=256)
    current_job = fields.Char('Current Job', size=256)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
