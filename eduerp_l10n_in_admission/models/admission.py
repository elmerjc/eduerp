# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api


class OpAdmission(models.Model):
    _inherit = 'op.admission'
    _description = "Admission"

    religion_id = fields.Many2one(
        'op.religion', 'Religion', states={'done': [('readonly', True)]})
    category_id = fields.Many2one(
        'op.category', 'Category', states={'done': [('readonly', True)]})
    is_old_student = fields.Boolean('Old Student?')
    gr_no_old = fields.Char('GR Number old', size=10)
    gr_no = fields.Char('GR Number new', size=10)

    @api.multi
    def get_student_vals(self):
        vals = super(OpAdmission, self).get_student_vals()
        gr = self.gr_no
        if self.is_old_student:
            gr = self.gr_no_old
        vals.update({
            'gr_no': gr,
            'category': self.category_id and self.category_id.id or False,
            'religion': self.religion_id and self.religion_id.id or False
        })
        return vals


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
