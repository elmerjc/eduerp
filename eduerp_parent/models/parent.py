# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpParent(models.Model):
    _name = 'op.parent'

    name = fields.Many2one(
        'res.partner', 'Name', default=lambda self: self.env[
            'res.partner'].search([('user_id', '=', self.env.uid)]),
        required=True)
    student_ids = fields.Many2many('op.student', string='Student(s)')
    user_id = fields.Many2one(
        'res.users', 'User', default=lambda self: self.env.uid, required=True)


class OpStudent(models.Model):

    _inherit = 'op.student'

    parent_ids = fields.Many2many('op.parent', string='Parent')


class ResUsers(models.Model):
    _inherit = "res.users"

    parent_ids = fields.One2many('op.parent', 'user_id', 'Parents')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
