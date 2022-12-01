# Copyright (c) 2022, ERP Cloud Systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TransportationTrip(Document):
	@frappe.whitelist()
	def on_submit(doc):
		pass
		'''
		new_doc = frappe.get_doc({
        "doctype": "Sales Invoice",
        "posting_date": doc.date,
        "customer": doc.customer,
        "cost_center": "13 - Main - TT",
        "taxes_and_charges": "KSA VAT 15% - T",
        "company": "Taazur Transportation",
        
		
        })


		items = new_doc.append("items", {})
		
		items.item_code = doc.trip
		items.qty = 1
		items.rate = doc.trip_cost
		items.income_account = "520301 - Transportation - AT - T"
		
		new_doc.insert(ignore_permissions=True)
		frappe.msgprint("  تم إنشاء فاتورة مبيعات بحالة مسودة رقم " + new_doc.name)
	'''
	@frappe.whitelist()
	def validate(doc):
		extras = frappe.db.sql(""" select name as name from `tabTransportation Request` where name = '{name}'""".format(name=doc.transportation_request), as_dict=1)
		for x in extras:
			frappe.db.set_value('Transportation Request', x.name, 'trip_statues', doc.workflow_state, update_modified=False)
		
		#set rate 
		rates = frappe.db.sql(""" select `tabItem Price`.price_list_rate as rate,  `tabItem Price`.item_code as item_code, `tabItem Price`.customer as customer
		                                                           from `tabItem Price` 
		                                                           
		                                                           where `tabItem Price`.item_code = '{name}'
																   and `tabItem Price`.customer = '{customer}'
																   and `tabItem Price`.selling = 1
		                                                       """.format(name=doc.trip, customer=doc.customer), as_dict=1)
		for z in rates :
			doc.trip_cost = z.rate
			#frappe.db.set_value('Transportation Trip', doc.name, 'trip_cost', z.rate, update_modified=False)