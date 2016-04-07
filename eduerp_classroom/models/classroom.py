# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpClassroom(models.Model):
    _name = 'op.classroom'

    name = fields.Char('Name', size=16, required=True)
    code = fields.Char('Code', size=4, required=True)
    course_id = fields.Many2one('op.course', 'Course', required=True)
    capacity = fields.Integer(string='No of Person')
    facilities = fields.One2many(
        'op.facility.line', 'classroom_id', string='Facility Lines')
    asset_line = fields.One2many('op.asset', 'asset_id', 'Asset')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
