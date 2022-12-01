# Copyright (c) 2022, ERP Cloud Systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class NewTimeSheet(Document):
	

	def on_submit(self):
		user = frappe.session.user
		lang = frappe.db.get_value("User", {'name': user}, "language")
		for x in self.time_sheet_details:
			new_doc2 = frappe.get_doc({
					"doctype": "Additional Salary",
					"employee": self.employee,
					"department": self.department,
					"salary_component": x.salary_component,
					"payroll_date": self.posting_date,
					"company":self.company,
					"amount": x.amount,
                    "time_sheet":self.name,
				})
			new_doc2.insert(ignore_permissions=True)
			new_doc2.submit()
			if lang == "ar":
				frappe.msgprint("  تم إنشاء راتب اضافى رقم " + new_doc2.name)
			else:
				frappe.msgprint(" Additional Salary " + new_doc2.name + " Created ")