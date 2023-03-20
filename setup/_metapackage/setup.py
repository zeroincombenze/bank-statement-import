import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-bank-statement-import",
    description="Meta package for oca-bank-statement-import Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-account_bank_statement_clear_partner',
        'odoo12-addon-account_bank_statement_import_bypass_check',
        'odoo12-addon-account_bank_statement_import_camt_oca',
        'odoo12-addon-account_bank_statement_import_move_line',
        'odoo12-addon-account_bank_statement_import_ofx',
        'odoo12-addon-account_bank_statement_import_online',
        'odoo12-addon-account_bank_statement_import_online_paypal',
        'odoo12-addon-account_bank_statement_import_online_ponto',
        'odoo12-addon-account_bank_statement_import_online_qonto',
        'odoo12-addon-account_bank_statement_import_online_transferwise',
        'odoo12-addon-account_bank_statement_import_paypal',
        'odoo12-addon-account_bank_statement_import_save_file',
        'odoo12-addon-account_bank_statement_import_split',
        'odoo12-addon-account_bank_statement_import_transfer_move',
        'odoo12-addon-account_bank_statement_import_txt_xlsx',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
