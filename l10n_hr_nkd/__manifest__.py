# -*- coding: utf-8 -*-

{
    "name": """Croatia - NKD""",
    "summary": """Hrvatska - Nacionalna Klasifikacija Djelatnosti""",
    "category": "Localisation / Croatia",
    "images": [],
    "version": "12.0.0.0.1",
    "application": False,

    "author": "DAJ MI 5!",
    "support": "support@odoo-hrvatska.org",
    "website": "http://odoo-hrvatska.org",
    "licence": "LGPL-3",
    #"price" : 20.00,   #-> only if module if sold!
    #"currency": "EUR",

    "depends": ['l10n_hr_base'],
    "external_dependencies": {
        "python": [],
        "bin": []
    },
    "data": [
        "views/res_company_view.xml",
        "views/res_partner_view.xml",
        "views/l10n_hr_nkd_view.xml",
        "data/l10n.hr.nkd.csv",
        "security/ir.model.access.csv",
    ],
    "qweb": [],
    "demo": [],

    "auto_install": False,
    "installable": True,
}

