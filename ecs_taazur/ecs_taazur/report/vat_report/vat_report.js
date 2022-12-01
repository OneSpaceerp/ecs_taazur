// Copyright (c) 2022, ERP Cloud Systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["VAT Report"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_start_date"),
			"reqd": 1
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_end_date"),
			"reqd": 1
		},
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options" : "Company",
			"reqd": 0
		},
		{
			"fieldname":"account",
			"label": __("Account"),
			"fieldtype": "Select",
			"options" : ["2401 - VAT 15%", "2402 - VAT 15% Restaurant%", "2403 - VAT 5%","2404 - VAT 5% Restaurant%" , "2405 - VAT Exempted%" , "2406 - VAT Zero%"],
			"reqd": 1
		}
	]
}

