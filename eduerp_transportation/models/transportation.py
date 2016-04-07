# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class OpTransportation(models.Model):
    _name = 'op.transportation'

    name = fields.Char('Name', size=64, required=True)
    stop_ids = fields.Many2many('op.stop', string='Stops')
    cost = fields.Float('Cost')
    vehicle_id = fields.Many2one('op.vehicle', 'Vehicle', required=True)
    start_time = fields.Float('Start Time', required=True)
    end_time = fields.Float('End Time', required=True)
    from_stop_id = fields.Many2one('op.stop', 'From', required=True)
    to_stop_id = fields.Many2one('op.stop', 'To', required=True)
    student_ids = fields.Many2many('op.student', string='Student(s)')

    @api.constrains('student_ids', 'vehicle_id')
    def check_capacity(self):
        if len(self.student_ids) > self.vehicle_id.capacity:
            raise ValidationError('Students over than vehicle capacity.')

    @api.constrains('from_stop_id', 'to_stop_id')
    def check_places(self):
        if self.from_stop_id == self.to_stop_id:
            raise ValidationError('To place cannot be equal to From place.')

    @api.constrains('start_time', 'end_time')
    def _check_date_time(self):
        if self.start_time < 0 or self.end_time < 0:
            raise ValidationError("Enter proper Time.")
        elif self.start_time > 24 or self.end_time > 24:
            raise ValidationError("Time can't be greater than 24 hours.")
        elif self.start_time >= self.end_time:
            raise ValidationError(
                'End Time cannot be set before or equal to Start Time.')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
