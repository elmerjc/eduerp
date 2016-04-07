# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################

from openerp import models, fields


class OpCourse(models.Model):
    _inherit = 'op.course'

    payment_term = fields.Many2one('account.payment.term', 'Payment Term')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
