{
    'name': 'Integrated Calendar',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Integrate various calendar views in Odoo into a single calendar app',
    'author': 'Simplify-ERP™',
    'website': 'https://simplify-erp.de',
    'depends': ['calendar', 'sale', 'stock', 'helpdesk', 'project'],
    'data': [
        'views/integrated_calendar_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
