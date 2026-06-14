

# -*- coding: utf-8 -*-

{
    'name': 'Saudi Tax Invoice — ZATCA Phase 2 | Bilingual | SAR Symbol | Custom Header & Footer',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Localizations',
    'author': 'CorePulse',
    'website': 'https://corepulse.sa',
    'depends': ['account', 'l10n_gcc_invoice', 'l10n_sa_edi'],
    'data': [
        'views/res_company_views.xml',
        'report/custom_invoice_report.xml',
        'report/cp_tax_invoice_report.xml',
        "invoice_report/report_invoice_odoo_standard.xml",
    ],
    'assets': {
        'web.report_assets_common': [
            'corepulse_tax_invoice_print/static/fonts/Tajawal-Regular.ttf',
            'corepulse_tax_invoice_print/static/fonts/Tajawal-Bold.ttf',
        ],
    },
    'demo': [],
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1',
    'price': 85.99,
    'currency': 'USD',
    'images': ['static/description/banner.png'],
}
