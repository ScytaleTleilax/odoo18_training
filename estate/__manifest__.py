{
    'name': 'Estate Management',
    'version': '1.0',
    'category': 'Real Estate',
    'sequence': 10,
    'summary': 'Manage properties and real estate listings',
    'website': 'https://github.com/ScytaleTleilax/odoo18_training',

    'depends': [
        'base',
        'base_setup',
    ],

    'data': [
        'security/ir.model.access.csv'
        # 'security/crm_security.xml',
        # 'data/crm_lead_merge_template.xml',
        # 'views/calendar_views.xml',
    ],
    'installable': True,
    'application': True,

    'assets': {
        'web.assets_backend': [
            # 'crm/static/src/**',
            # ('remove', 'crm/static/src/views/forecast_graph/**'),
            # ('remove', 'crm/static/src/views/forecast_pivot/**'),
        ],
        'web.assets_backend_lazy': [
            # 'crm/static/src/views/forecast_graph/**',
            # 'crm/static/src/views/forecast_pivot/**',
        ],
    },
    'author': 'andreivradulescu@gmail.com',
    'license': 'LGPL-3',
}
