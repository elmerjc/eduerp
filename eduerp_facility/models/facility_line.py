# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class OpFacilityLine(models.Model):
    _name = 'op.facility.line'
    _rec_name = 'facility_id'

    facility_id = fields.Many2one('op.facility', 'Facility', required=True)
    quantity = fields.Float('Quantity', required=True)

    @api.constrains('quantity')
    def check_quantity(self):
        if self.quantity <= 0.0:
            raise ValidationError("Enter proper Quantity in Facilities!")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
