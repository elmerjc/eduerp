# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from openerp import models, fields, api
from openerp.exceptions import ValidationError


class TimeTableReport(models.TransientModel):
    _name = 'time.table.report'
    _description = 'Generate Time Table Report'

    state = fields.Selection(
        [('faculty', 'Faculty'), ('student', 'Student')],
        string='Select', required=True, default='faculty')
    course_id = fields.Many2one('op.course', 'Course')
    batch_id = fields.Many2one('op.batch', 'Batch')
    faculty_id = fields.Many2one('op.faculty', 'Faculty')
    start_date = fields.Date(
        'Start Date', required=True,
        default=(datetime.today() - relativedelta(
            days=datetime.date(
                datetime.today()).weekday())).strftime('%Y-%m-%d'))
    end_date = fields.Date(
        'End Date', required=True,
        default=(datetime.today() + relativedelta(days=6 - datetime.date(
            datetime.today()).weekday())).strftime('%Y-%m-%d'))

    @api.one
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        start_date = fields.Date.from_string(self.start_date)
        end_date = fields.Date.from_string(self.end_date)
        if end_date < start_date:
            raise ValidationError('End Date cannot be set before Start Date.')
        elif end_date > (start_date + timedelta(days=6)):
            raise ValidationError("Select date range for a week!")

    @api.onchange('course_id')
    def onchange_course(self):
        self.batch_id = False

    @api.multi
    def gen_time_table_report(self):
        data = self.read(
            ['start_date', 'end_date', 'course_id', 'batch_id', 'state',
             'faculty_id'])[0]
        if data['state'] == 'student':
            time_table_ids = self.env['op.timetable'].search(
                [('course_id', '=', data['course_id'][0]),
                 ('batch_id', '=', data['batch_id'][0]),
                 ('start_datetime', '>', data['start_date'] + '%H:%M:%S'),
                 ('end_datetime', '<', data['end_date'] + '%H:%M:%S')],
                order='start_datetime asc')

            data.update({'time_table_ids': time_table_ids.ids})
            return self.env['report'].get_action(
                self, 'eduerp_timetable.report_timetable_student_generate',
                data=data)
        else:
            teacher_time_table_ids = self.env['op.timetable'].search(
                [('start_datetime', '>', data['start_date'] + '%H:%M:%S'),
                 ('end_datetime', '<', data['end_date'] + '%H:%M:%S'),
                 ('faculty_id', '=', data['faculty_id'][0])],
                order='start_datetime asc')

            data.update({'teacher_time_table_ids': teacher_time_table_ids.ids})
            return self.env['report'].get_action(
                self, 'eduerp_timetable.report_timetable_teacher_generate',
                data=data)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
