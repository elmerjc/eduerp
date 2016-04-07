# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class OpScholarshipType(models.Model):
    _name = 'op.scholarship.type'

    name = fields.Char('Name', size=64, required=True)
    amount = fields.Integer('Amount')

    @api.constrains('amount')
    def check_amount(self):
        if self.amount <= 0:
            raise ValidationError('Enter proper Amount')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
