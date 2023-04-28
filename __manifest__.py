
{
    'name': 'Integrated Calendar',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Integrate various calendar views in Odoo into a single calendar app',
    'author': "Simplify-ERP",

    'website': 'https://simplify-erp.de',
    'depends': [
        'base',
        'calendar',
    ],
    'external_dependencies': {"python": ["mako"]},

    'data': [
        'views/super_calendar_view.xml',
        'data/cron_data.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
