# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpHealthLine(models.Model):
    _name = 'op.health.line'

    health_id = fields.Many2one('op.health', 'Health')
    date = fields.Date('Date', default=lambda self: fields.Date.today())
    name = fields.Text('Checkup Detail', required=True)
    recommendation = fields.Text('Checkup Recommendation')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
