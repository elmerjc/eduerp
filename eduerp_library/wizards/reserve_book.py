# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields, api


class ReserveBook(models.TransientModel):

    """ Reserve Book """
    _name = 'reserve.book'

    partner_id = fields.Many2one('res.partner', required=True)

    @api.one
    def set_partner(self):
        self.env['op.book.movement'].browse(
            self.env.context.get('active_ids', False)).write(
            {'partner_id': self.partner_id.id,
             'reserver_name': self.partner_id.name, 'state': 'reserve'})


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
