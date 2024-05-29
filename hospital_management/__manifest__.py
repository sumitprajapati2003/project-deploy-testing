{
    'name': "Hospital Management",
    'version': '17.0.0.1',
    'author': "OpenEduCat Inc",
    'category': 'hospital',
    'description': """  Hospital """,
    'data': [
        "security/ir.model.access.csv",
        "security/hospital_security.xml",

        # "data/dr.specialties.csv",
        # "data/patient.disease.csv",

        # DEMO DATA FILES

        "data/ir_sequence.xml",
        "data/dr_specialties_data.xml",
        "data/patient_disease_data.xml",
        "data/department_data.xml",
        "data/doctor_data.xml",
        "data/week_day_data.xml",

        # MAIL TEMPLATE
        "data/blood_request_fullfilled_mail_template.xml",
        "data/ir_cron.xml",
        "data/appointment_reminder_mail.xml",

        #VIEWS FILES

        # "view/patient.xml",
        # "view/doctor.xml",
        "view/specialties.xml",
        "view/disease.xml",
        "view/department.xml",
        "view/res_partner.xml",
        "view/staff.xml",
        "view/doctor_availability.xml",
        "view/blood_donor.xml",
        "view/blood_bank.xml",
        "view/blood_request.xml",
        "view/appointment.xml",
        "menu/menu.xml",
    ],
    'depends': [
        'mail',
        'contacts',
        'base',
        ],
    'demo': [
        
        # "demo/patient_demo.xml",
    ],
    'installable':True,
    'auto_install':False,
    'application':True,
    "license":"LGPL-3"
}