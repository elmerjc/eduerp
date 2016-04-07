# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class StudentAttendance(models.TransientModel):
    _name = 'student.attendance'

    from_date = fields.Date(
        'From Date', required=True, default=lambda self: fields.Date.today())
    to_date = fields.Date(
        'To Date', required=True, default=lambda self: fields.Date.today())

    @api.one
    @api.constrains('from_date', 'to_date')
    def check_dates(self):
        from_date = fields.Date.from_string(self.from_date)
        to_date = fields.Date.from_string(self.to_date)
        if to_date < from_date:
            raise ValidationError("To Date cannot be set before From Date.")

    @api.multi
    def print_report(self):
        data = self.read(['from_date', 'to_date'])[0]
        data.update({'student_id': self.env.context.get('active_id', False)})

        return self.env['report'].get_action(
            self, 'eduerp_attendance.student_attendance_report', data=data)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
