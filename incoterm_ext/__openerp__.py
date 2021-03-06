#!/usr/bin/python                                                               
# -*- encoding: utf-8 -*-                                                       
############################################################################### 
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) Vauxoo (<http://vauxoo.com>).
#    All Rights Reserved                                                        
################# Credits###################################################### 
#    Coded by: Maria Gabriela Quilarque <gabriela@vauxoo.com>                                   
#              Luis Escobar <luis@vauxoo.com>
#    Audited by: Nhomar Hernandez <nhomar@vauxoo.com>
############################################################################### 
#    This program is free software: you can redistribute it and/or modify       
#    it under the terms of the GNU Affero General Public License as published   
#    by the Free Software Foundation, either version 3 of the License, or       
#    (at your option) any later version.                                        
#                                                                               
#    This program is distributed in the hope that it will be useful,            
#    but WITHOUT ANY WARRANTY; without even the implied warranty of             
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              
#    GNU Affero General Public License for more details.                        
#                                                                               
#    You should have received a copy of the GNU Affero General Public License   
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.      
###############################################################################    
{
    "name" : "Incoterm Decription",
    "version" : "0.1",
    "depends" : ["sale", "stock"],
    "author" : "Vauxoo",
    "description" : """
    Add Formal Description to Incoterms.
                    """,
    "website" : "http://vauxoo.com",
    "category" : "Generic Modules/Sales",
    "data" : [
        "incoterm_view.xml",
    ],
    "active": False,
    "installable": True,
}
