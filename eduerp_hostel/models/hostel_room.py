# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class OpHostelRoomAllocation(models.Model):
    _name = 'op.hostel.room'

    hostel_id = fields.Many2one('op.hostel', 'Hostel', required=True)
    name = fields.Many2one('op.room', 'Room', required=True)
    student_ids = fields.Many2many('res.partner', string='Allocated Students')
    students_per_room = fields.Integer('Students per Room', required=True)
    rent = fields.Float('Rent')
    allocated_date = fields.Date('Allocated Date', default=fields.Date.today())

    @api.constrains('students_per_room')
    def check_capacity(self):
        if self.students_per_room <= 0:
            raise ValidationError("Enter proper Student Per Room")

    @api.onchange('hostel_id')
    def onchange_hostel(self):
        if self.hostel_id:
            self.name = False

    @api.onchange('name')
    def onchange_name(self):
        if self.name:
            self.students_per_room = self.name.capacity

    @api.one
    @api.constrains('student_ids', 'students_per_room')
    def _check_student_capacity(self):
        if len(self.student_ids) > self.students_per_room:
            raise ValidationError('Room capacity Over')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
