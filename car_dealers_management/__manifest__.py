{
    "name":"Car Dealers Management",
    "version":"17.0",
    "summary":"This is Car Dealers Management",
    "description":"""""",
    "depends":['fleet','mail','website'],
    "data":[
        'security/ir.model.access.csv',
        'data/website_menu.xml',
        'views/sell_buy_view.xml',
        'views/car_enquire_view.xml',
        'wizard/car_enquire_wizard.xml',
        'views/car_enquire_template.xml',
        'views/car_sell_buy_template.xml',
        'views/tracking_template.xml',
        'views/menu_view.xml',
        'data/sell_buy_mail_template.xml',
        # 'report/sell_buy_report_templates.xml',
        # 'report/sell_buy_report.xml',
       
    ],
    'license': 'LGPL-3',
    'demo':[
        

    ],
    "installable":True,
    "auto_install":False,
    "application":True
}