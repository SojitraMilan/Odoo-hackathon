{
    'name': 'StackIt Q&A Platform',
    'version': '1.0',
    'summary': 'Minimal Q&A Forum for Collaborative Learning',
    'description': """
        StackIt is a minimal question-and-answer platform that supports collaborative learning and structured knowledge sharing.
    """,
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'category': 'Website/Forum',
    'depends': ['base', 'web', 'mail', 'portal'],
    'data': [
        'security/security_rules.xml',
        'security/ir.model.access.csv',
        'views/question_views.xml',
        'views/answer_views.xml',
        'views/tag_views.xml',
        'views/notification_views.xml',
        'views/templates.xml',
        'views/assets.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}