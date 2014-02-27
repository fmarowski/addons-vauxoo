# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2012 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info@vauxoo.com
############################################################################
#    Coded by: moylop260 (moylop260@vauxoo.com)
#    Coded by: isaac (isaac@vauxoo.com)
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

{
    "name" : "Product Price Visible",
    "version" : "1.0",
    "author" : "Vauxoo",
    "category" : "Product",
    "description" : """This module add group to products prices
    """,
    "website" : "www.vauxoo.com",
    "license" : "AGPL-3",
    "depends" : ["stock"],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
            "security/product_price_visible.xml",
            #~ "security/ir.model.access.csv",
            "product_view.xml",],
    "installable" : True,
    "active" : False,
}
