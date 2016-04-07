# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class OpHostel(models.Model):
    _name = 'op.hostel'

    name = fields.Char('Name', size=16, required=True)
    capacity = fields.Integer('Hostel Capacity', required=True)
    hostel_room_lines = fields.One2many(
        'op.hostel.room', 'hostel_id', 'Room(s)')

    @api.one
    @api.constrains('hostel_room_lines')
    def _check_hostel_capacity(self):
        if self.capacity <= 0:
            raise ValidationError('Enter proper Hostel Capacity')
        counter = 0.00
        for room in self.hostel_room_lines:
            counter += room.students_per_room
            if counter > self.capacity:
                raise ValidationError('Hostel Capacity Over')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
