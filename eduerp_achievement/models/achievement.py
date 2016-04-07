# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpAchievement(models.Model):
    _name = 'op.achievement'
    _rec_name = 'student_id'

    student_id = fields.Many2one('op.student', 'Student', required=True)
    faculty_id = fields.Many2one('op.faculty', 'Faculty', required=True)
    achievement_type = fields.Many2one(
        'op.achievement.type', 'Achievement Type', required=True)
    description = fields.Text('Description', required=True)
    achievement_date = fields.Date(
        'Date', required=True, default=fields.Date.today())

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
