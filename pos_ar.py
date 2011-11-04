# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2008-2011
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from osv import osv, fields
 
class invoice_denomination(osv.osv):
    _name = "invoice.denomination"
    _description = "Denomination for Invoices"
    _columns = { 
        'name' : fields.char('Denomination', required=True, size=4),
        'desc' : fields.char('Description', required=True, size=100),
    }
    _sql_constraints = [
        ('code_denomination_uniq', 'unique (name)', 'The Denomination of the Invoices must be unique per company !')
    ]
invoice_denomination()
    
class pos_ar(osv.osv):
    _name = "pos.ar"
    _description = "Point of Sale for Argentina"
    _columns = {
        'name' : fields.char('Nro', required=True, size=6),
        'desc' : fields.char('Description', required=True, size=180),
        'priority' : fields.integer('Priority', required=True, size=6),
        'shop_id': fields.many2one('sale.shop', 'Shop', required=True),
        'denomination_id': fields.many2one('invoice.denomination', 'Denomination'),
    }
     
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['name', 'desc'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['desc']:
                name = name + ' - '+ record['desc']
            res.append((record['id'], name))
        return res
        
pos_ar()
