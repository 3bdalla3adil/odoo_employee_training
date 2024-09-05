# -*- coding: utf-8 -*-
{
    'name': "Employee Training Records",

    'summary': "custom module in Odoo to manage Employee Training Records",

    'description': """
     Assuming that each employee  """,
    'author': "Eng. Abdulla Bashir",
    'website': "https://www.3bdalla3adil.github.io",
    'category': 'Human Resources',
    'version': '0.1',

    'depends': ['hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/training_course_views.xml',
        # 'views/training_record_views.xml',
        'views/training_plan_views.xml',

        'views/employee_skill_views.xml',

        'views/hr_employee_views.xml',
        
        'views/automated_actions.xml',
        'views/email_templates.xml',
        'views/report_training_history.xml',
    ],
    'installable': True,
    'application': True,
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}

