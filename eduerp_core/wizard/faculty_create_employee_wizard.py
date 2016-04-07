# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api


class WizardOpFacultyEmployee(models.TransientModel):
    _name = 'wizard.op.faculty.employee'
    _description = "Create Employee and User of Faculty"

    user_boolean = fields.Boolean("Want to create user too ?", default=True)

    @api.one
    def create_employee(self):
        active_id = self.env.context.get('active_ids', []) or []
        record = self.env['op.faculty'].browse(active_id)
        record.create_employee()
        if self.user_boolean and not record.user_id:
            user_group = self.env.ref('eduerp_core.group_op_faculty')
            self.env['res.users'].create_user(record, user_group)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
