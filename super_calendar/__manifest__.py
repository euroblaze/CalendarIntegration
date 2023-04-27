
{
    'name': 'Integrated Calendar',
    'version': '1.0.1',
    'category': 'Generic Modules/Others',
    'summary': 'This module allows to create configurable calendars.',
    'author': "Issa Mehrez",

    'website': '',
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
