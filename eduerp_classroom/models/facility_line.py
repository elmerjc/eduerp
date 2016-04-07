# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpFacilityLine(models.Model):

    _inherit = 'op.facility.line'

    classroom_id = fields.Many2one('op.classroom', 'Classroom')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
