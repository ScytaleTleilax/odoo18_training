{
    'name': 'Estate Management',
    'version': '1.0',
    'category': 'Real Estate',
    'sequence': 10,
    'summary': 'Manage properties and real estate listings',
    'website': 'https://github.com/ScytaleTleilax/odoo18_training',

    'depends': [
        'base'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_actions.xml',
        'views/estate_menus.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
        ],
        'web.assets_backend_lazy': [
        ],
    },
    'author': 'andreivradulescu@gmail.com',
    'license': 'LGPL-3',
}
