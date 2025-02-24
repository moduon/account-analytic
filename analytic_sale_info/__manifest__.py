# Copyright 2025 Moduon Team S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

{
    "name": "Analytic Sale Info",
    "summary": "Extra analytic information gathered from related sale order lines",
    "version": "16.0.1.0.0",
    "development_status": "Alpha",
    "category": "Accounting/Accounting",
    "website": "https://github.com/OCA/account-analytic",
    "author": "Moduon, Odoo Community Association (OCA)",
    "maintainers": ["yajo", "rafaelbn"],
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "preloadable": True,
    "auto_install": False,
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
    "post_load": "post_load",
    "uninstall_hook": "uninstall_hook",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
    ],
    "excludes": [
        "incompatible_module_name",
    ],
    "data": [
        "security/some_model_security.xml",
        "security/ir.model.access.csv",
        "views/report_name.xml",
        "views/model_name_view.xml",
        "wizards/wizard_model_view.xml",
    ],
    "demo": [
        "demo/assets.xml",
        "demo/model_name_demo.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "module/static/src/css/module_name.css",
            "module/static/src/js/module_name.js",
        ],
        "web.qunit_suite_tests": [
            "module/static/src/js/*.tour.js",
        ],
    },
}
