# -*- coding: utf-8 -*-

{
    "name": """Croatia - base""",
    "summary": """Croatia base localization data""",
    "category": "Localisation / Croatia",
    "images": [],
    "version": "10.0.0.0",
    "application": False,

    "author": "Odoo Hrvatska, ",
    "support": "support@odoo-hrvatska.org",
    "website": "http://odoo-hrvatska.org",
    "licence": "LGPL-3",
    #"price" : 20.00,   #-> only if module if sold!
    #"currency": "EUR",

    "depends": [
        #"report"
    ],
    "external_dependencies": {
        "python": [
            'tzlocal'
        ],
        "bin": []
    },
    "data": [
        "views/res_company_view.xml",

        # NKD
        #"views/l10n_hr_nkd_view.xml",
        #"data/localization_settings.xml",
        #"security/ir.model.access.csv",
    ],
    "qweb": [],
    "demo": [],

    "auto_install": False,
    "installable": True,
}

