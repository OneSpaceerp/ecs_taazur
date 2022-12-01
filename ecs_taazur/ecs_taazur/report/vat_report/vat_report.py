# Copyright (c) 2013, erpcloud.systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_data(filters, columns)
    return columns, data


def get_columns():
    return [
        {
            "label": _("Company"),
            "fieldname": "company",
            "fieldtype": "Link",
            "options": "Company",
            "width": 200
        },

        {
            "label": _("Date"),
            "fieldname": "posting_date",
            "fieldtype": "Date",
            "width": 100
        },
        {
            "label": _("Account"),
            "fieldname": "account",
            "fieldtype": "Link",
            "options": "Account",
            "width": 200
        },

        {
            "label": _("Voucher Type"),
            "fieldname": "voucher_type",
            "fieldtype": "Data",
            "width": 130
        },
        {
            "label": _("Voucher No"),
            "fieldname": "voucher_no",
            "fieldtype": "Dynamic Link",
            "options": "voucher_type",
            "width": 180
        },
        {
            "label": _("Debit"),
            "fieldname": "debit",
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "label": _("Credit"),
            "fieldname": "credit",
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "label": _("Balance"),
            "fieldname": "balance",
            "fieldtype": "Float",
            "width": 150
        }

    ]


def get_data(filters, columns):
    item_price_qty_data = []
    item_price_qty_data = get_item_price_qty_data(filters)
    return item_price_qty_data


def get_item_price_qty_data(filters):
    conditions = ""
    if filters.get("from_date"):
        conditions += " and `tabGL Entry`.posting_date>=%(from_date)s"
    if filters.get("to_date"):
        conditions += " and `tabGL Entry`.posting_date<=%(to_date)s"
    if filters.get("company"):
        conditions += " and `tabGL Entry`.company =%(company)s"
    if filters.get("account"):
        conditions += " and `tabGL Entry`.account like %(account)s"
    item_results = frappe.db.sql("""
				select
						`tabGL Entry`.company as company,
						`tabGL Entry`.posting_date as posting_date,
						`tabGL Entry`.account as account,
						`tabGL Entry`.voucher_type as voucher_type,
						`tabGL Entry`.voucher_no as voucher_no,
						`tabGL Entry`.debit as debit,
						`tabGL Entry`.credit as credit

				from
				`tabGL Entry`

				where
				`tabGL Entry`.docstatus = 1
				and `tabGL Entry`.is_cancelled = 0
				{conditions}
				
                order by
				`tabGL Entry`.posting_date asc



				""".format(conditions=conditions), filters, as_dict=1)

    # price_list_names = list(set([item.price_list_name for item in item_results]))

    # buying_price_map = get_price_map(price_list_names, buying=1)
    # selling_price_map = get_price_map(price_list_names, selling=1)

    result = []
    if item_results:
        for item_dict in item_results:
            data = {
                'company': item_dict.company,
                'posting_date': _(item_dict.posting_date),
                'voucher_type': _(item_dict.voucher_type),
                'voucher_no': _(item_dict.voucher_no),
                'account': _(item_dict.account),
                'debit': item_dict.debit,
                'credit': item_dict.credit,
                'balance': item_dict.debit - item_dict.credit,

            }
            result.append(data)

    return result
