# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class OpExamRoom(models.Model):
    _name = 'op.exam.room'

    name = fields.Char('Name', size=256, required=True)
    classroom_id = fields.Many2one('op.classroom', 'Classroom', required=True)
    capacity = fields.Integer('Capacity', required=True)
    course_ids = fields.Many2many('op.course', string='Course(s)')
    student_ids = fields.Many2many('op.student', string='Student(s)')

    @api.constrains('capacity')
    def check_capacity(self):
        if self.capacity < 0:
            raise ValidationError('Enter proper Capacity')
        elif self.capacity > self.classroom_id.capacity:
            raise ValidationError('Capacity over Classroom capacity!')

    @api.onchange('classroom_id')
    def onchange_classroom(self):
        self.capacity = self.classroom_id.capacity

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
