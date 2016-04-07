# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from datetime import datetime
import time

from openerp import models, pooler
from openerp.report import report_sxw


class TimeTableTeacherGenerate(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context=None):
        super(TimeTableTeacherGenerate, self).__init__(
            cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'get_object': self.get_object,
            'get_full_name': self.get_full_name,
        })

    def get_full_name(self, data):
        faculty_name = self.pool.get('op.faculty').browse(
            self.cr, self.uid, data['faculty_id'][0])
        return ' '.join([faculty_name.name,
                         faculty_name.middle_name,
                         faculty_name.last_name])

    def sort_tt(self, data_list):
        main_list = []
        f = []
        for d in data_list:
            if d['period'] not in f:
                f.append(d['period'])
                main_list.append({
                    'name': d['period'],
                    'line': {d['day']: d},
                    'peropd_time': ' To '.join([d['start_datetime'],
                                                d['end_datetime']])
                })
            else:
                for m in main_list:
                    if m['name'] == d['period']:
                        m['line'][d['day']] = d
        return main_list

    def get_object(self, data):

        dayofWeek = ['Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday', 'Sunday']

        data_list = []
        for timetable_obj in pooler.get_pool(self.cr.dbname).get(
            'op.timetable').browse(
                self.cr, self.uid, data['teacher_time_table_ids']):
            oldDate = datetime.strptime(
                timetable_obj.start_datetime, "%Y-%m-%d %H:%M:%S")
            day = dayofWeek[datetime.weekday(oldDate)]

            timetable_data = {
                'period': timetable_obj.period_id.name,
                'period_time': timetable_obj.period_id.hour + ':' +
                timetable_obj.period_id.minute +
                timetable_obj.period_id.am_pm,
                'sequence': timetable_obj.period_id.sequence,
                'start_datetime': timetable_obj.start_datetime,
                'end_datetime': timetable_obj.end_datetime[10:],
                'day': day,
                'subject': timetable_obj.subject_id.name,
                'course': timetable_obj.course_id.name,
                'batch': timetable_obj.batch_id.name,
            }
            data_list.append(timetable_data)

        ttdl = sorted(data_list, key=lambda k: k['sequence'])
        final_list = self.sort_tt(ttdl)
        return final_list


class ReportTimeTableTeacherGenerate(models.AbstractModel):
    _name = 'report.eduerp_timetable.report_timetable_teacher_generate'
    _inherit = 'report.abstract_report'
    _template = 'eduerp_timetable.report_timetable_teacher_generate'
    _wrapped_report_class = TimeTableTeacherGenerate


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
