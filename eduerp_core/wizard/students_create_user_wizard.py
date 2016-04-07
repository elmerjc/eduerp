# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api


class WizardOpStudent(models.TransientModel):
    _name = 'wizard.op.student'
    _description = "Create User for selected Student(s)"

    def _get_students(self):
        if self.env.context and self.env.context.get('active_ids'):
            return self.env.context.get('active_ids')
        return []

    student_ids = fields.Many2many(
        'op.student', default=_get_students, string='Students')

    @api.one
    def create_student_user(self):
        user_group = self.env.ref('eduerp_core.group_op_student')
        active_ids = self.env.context.get('active_ids', []) or []
        records = self.env['op.student'].browse(active_ids)
        self.env['res.users'].create_user(records, user_group)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
