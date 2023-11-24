{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Sales/Real Estate',
    'summary': 'My summary',
    'description': 'My description',
    'website': 'https://localhost/page/state',
    'depends': [
        'base_setup',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}