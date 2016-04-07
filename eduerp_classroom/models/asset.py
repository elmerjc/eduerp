# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

from openerp import models, fields


class OpAsset(models.Model):
    _name = 'op.asset'

    asset_id = fields.Many2one('op.classroom', 'Asset')
    product_id = fields.Many2one('product.product', 'Product', required=True)
    code = fields.Char('Code', size=256)
    product_uom_qty = fields.Float('Quantity', required=True)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
