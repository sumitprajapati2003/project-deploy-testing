{
    "name": "Training and placement",
    'category': 'Education',
    'version': '17.0.0.1',
    'sequence':1,
    "summary": "training and placement for student",
    'website': 'https://www.openeducat.org',
    "description": "training and placement for student",
    "author":"OpenEduCat Inc",
    "depends": [
        'mail',
        'contacts',
        'sale',
        'website'
    ],
    "data": [
        "security/ir.model.access.csv",
        
        "data/ir_sequence.xml",
        "data/ir_cron.xml",
        "data/website_menu.xml",
        
        
        
        "views/application_view.xml",
        "views/authority_view.xml",
        "views/company_view.xml",
        "views/course_view.xml",
        "views/placement_view.xml",
        "views/session_view.xml",
        "views/trainee_view.xml",
        "views/res_partner_view.xml",
        "views/course_fee_wizard_view.xml",
        "views/session_report_wizard_view.xml",
        # "reports/report_wizard_session_template.xml",
        "views/placement_wizard_view.xml",
        "views/multi_step_wizard.xml",
        "views/course_template.xml",
        
        
        "reports/report.xml",
        "reports/report_template.xml",
        "reports/report_application.xml",
        "reports/report_application_template.xml",
        "reports/report_placement.xml",
        "reports/report_placement_template.xml",
        "reports/report_company.xml",
        "reports/report_company_template.xml",
        "reports/sale_report_inherit.xml",
        
        "menu/menu.xml"

    ],
    "demo":[
        "demo/trainee_demo.xml",
        "demo/course_demo.xml",
        "demo/company_demo.xml",
        "demo/company_career_demo.xml"
     
    ],
    'application': True,
    "installable":True,
    "license":"LGPL-3",
}