# -*- coding: utf-8 -*-
{
    "name": "Croatia - Accounting base",
    "summary": "Croatia accounting localisation",
    "category": "Localisation / Croatia",
    "images": [],
    "version": "10.0.0.0.1",
    "application": False,

    "author": "Decod.io",
    "support": "support@odoo-hrvatska.org",
    "website": "http://odoo-hrvatska.org",
    "licence": "LGPL-3",
    #"price" : 20.00,   #-> only if module if sold!
    #"currency": "EUR",

    "depends": [
        "account",
       # "account_storno",
        "base_vat",
        "base_iban",
        "l10n_hr_base",
    ],
    "external_dependencies": {
        "python": [],
        "bin": []
    },
    "data": [
        "security/ir.model.access.csv",
        #"views/res_config_view.xml",
        "views/res_company_view.xml",
        "views/res_users_view.xml",
        "views/account_invoice_view.xml",
        "views/account_journal_view.xml",
        # #"views/report_invoice.xml",
        # "views/reports_menu.xml",

    ],
    "qweb": [],
    "demo": [],

    "auto_install": False,
    "installable": True,
}


