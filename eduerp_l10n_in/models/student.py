# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpStudent(models.Model):
    _inherit = 'op.student'

    category = fields.Many2one('op.category', 'Category')
    religion = fields.Many2one('op.religion', 'Religion')
    pan_card = fields.Char('PAN Card', size=16)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
