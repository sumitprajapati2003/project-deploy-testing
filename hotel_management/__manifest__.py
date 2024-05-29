{
    'name':'Hotel Management',
    'version':'17.0',
    'summary':'This Module For Hotel Management',
    'description':'Module For Members and Hotel Detail',
    'depends':['sale','mail',"website"],
    'data':[
        'security/hotel_security.xml',
        'security/ir.model.access.csv',
        'views/hotel_room_view.xml',
        'views/amenities_view.xml',
        'views/amenities_group_view.xml',
        'data/hotel_mail_template.xml',
        'wizard/room_book.xml',
        'report/hotel_report_template.xml',
        'report/hotel_report.xml',
        'views/dashboard.xml',
        'views/hotel_room_history_view.xml',

        'menu/hotel_menu.xml',
        'data/hotel_detail_menu.xml',
        'views/hotel_room_detail_template.xml',
        'views/book_room_form.xml',
        

    ],
    'demo':[],
    'auto_install':False,
    'installable':True,
    'application':True,
    'license': 'LGPL-3',
}