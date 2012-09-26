# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2012 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info@vauxoo.com
############################################################################
#    Coded by: fernandoL (fernando_ld@vauxoo.com)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from tools.translate import _
from osv import osv, fields
import decimal_precision as dp

class account_move(osv.osv):
    _inherit = "account.move"
    
    """equivalent query that get these fields ---
    select sum(credit) from account_move_line
    select sum(debit) from account_move_line
    """
    
    def _sum_credit(self, cr, uid, ids, field, arg, context=None):
        cr.execute("select sum(credit) from account_move_line")
        suma = cr.fetchone()
        dict = {}
        for line in ids:
            dict[line] = suma[0]
        return dict
    
    def _sum_debit(self, cr, uid, ids, field, arg, context=None):
        cr.execute("select sum(debit) from account_move_line")
        suma = cr.fetchone()
        dict = {}
        for line in ids:
            dict[line] = suma[0]
        return dict
    
    _columns = {
        'total_debit': fields.function(_sum_debit, string='Total debit', method=True, digits_compute=dp.get_precision('Account'), type='float'),
        'total_credit': fields.function(_sum_credit, string='Total credit', method=True, digits_compute=dp.get_precision('Account'), type='float'),
    }

account_move()