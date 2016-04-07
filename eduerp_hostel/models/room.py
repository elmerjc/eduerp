# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class OpRoom(models.Model):
    _name = 'op.room'

    hostel_id = fields.Many2one('op.hostel', 'Hostel', required=True)
    name = fields.Char('Room Name', required=True)
    code = fields.Char('Code', required=True)
    capacity = fields.Integer('Room Capacity', required=True)
    facility_line = fields.One2many('op.facility.line', 'room_id', 'Facility')

    @api.constrains('capacity')
    def check_capacity(self):
        if self.capacity <= 0:
            raise ValidationError('Enter proper Capacity')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
