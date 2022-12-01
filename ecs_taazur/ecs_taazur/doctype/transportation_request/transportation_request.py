# Copyright (c) 2022, ERP Cloud Systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TransportationRequest(Document):
	@frappe.whitelist()
	def on_submit(self):
		####Creat Draft Transportation Trip
		'''
		customer_data = frappe.db.sql(""" select `tabCustomer`.name as name, `tabCustomer`.mobile_no as phone,`tabCustomer`.email_id as email
																from `tabCustomer` 
																 where `tabCustomer`.disabled =	0												
																""".format(name=self.name), as_dict=1)
		for x in customer_data:
			phone = x.phone
			email = x.email
			name = x.name
		if self.phone == phone or self.email == email:
			customer_name = name
		else:
			new_doc = frappe.get_doc({
				"doctype": "Customer",
				"customer_name": self.full_name,
				"customer_type": "Company",
				"customer_group": "All Customer Groups",
				"territory": "All Territories",
				"mobile_no": self.phone,
				"email_id": self.email,
				"tax_id": 0,
				"default_currency": "SAR",
			})
			new_doc.insert(ignore_permissions=True)
			customer_name = new_doc.name
		'''
		new_doc2 = frappe.get_doc({
						"doctype": "Transportation Trip",
						"customer": self.customer,
						"transportation_request": self.name,
						"transportation_date": self.date,
						"vehicle_customer": self.vehicle,
						"from_location": self.from_location,
						"to_location": self.to_location,
						"goods_details": self.goods_details,
						"full_name": self.full_name,
						"receiver_email": self.receiver_email,
						"phone": self.phone,
						"address": self.address,
						})
		new_doc2.insert(ignore_permissions=True)