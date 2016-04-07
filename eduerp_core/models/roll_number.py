# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api


class OpRollNumber(models.Model):
    _name = 'op.roll.number'
    _rec_name = 'roll_number'

    roll_number = fields.Char('Roll Number', size=8, required=True)
    course_id = fields.Many2one('op.course', 'Course', required=True)
    batch_id = fields.Many2one('op.batch', 'Batch', required=True)
    student_id = fields.Many2one('op.student', 'Student', required=True)

    @api.onchange('student_id')
    def onchange_student(self):
        self.course_id = self.student_id.course_id
        self.batch_id = self.student_id.batch_id

    _sql_constraints = [
        ('unique_name_roll_number_id',
         'unique(roll_number,course_id,batch_id,student_id)',
         'Roll Number & Student must be unique per Batch!'),
        ('unique_name_roll_number_course_id',
         'unique(roll_number,course_id,batch_id)',
         'Roll Number must be unique per Batch!'),
        ('unique_name_roll_number_student_id',
         'unique(student_id,course_id,batch_id)',
         'Student must be unique per Batch!'),
    ]

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
