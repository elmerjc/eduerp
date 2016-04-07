# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class OpVehicle(models.Model):
    _name = 'op.vehicle'

    name = fields.Char('Name', size=16, required=True)
    reg_number = fields.Char('Registration Number', size=16,  required=True)
    capacity = fields.Integer('Capacity', required=True)
    active = fields.Boolean('Active', default=True)
    partner_id = fields.Many2one('res.partner', 'Driver')

    @api.constrains('capacity')
    def check_capacity(self):
        if self.capacity <= 0:
            raise ValidationError('Enter proper Capacity.')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
