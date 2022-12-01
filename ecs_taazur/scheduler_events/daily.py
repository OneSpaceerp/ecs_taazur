from __future__ import unicode_literals
import frappe
from frappe import _

frappe.whitelist()
def daily():
    vac_emp = frappe.db.sql(""" select employee as employee from `tabLeave Application` 
    where leave_type in ('Annual Leave (30)','Annual Leave (21)','Annual Leave (15)')
    and docstatus = 1
    and CURDATE() = from_date
    """,as_dict=1)
    for emp in vac_emp:
        frappe.db.sql(""" update `tabEmployee` set status = 'Suspended' where name = '{empo}'
        """.format(empo=emp.employee))
    pass