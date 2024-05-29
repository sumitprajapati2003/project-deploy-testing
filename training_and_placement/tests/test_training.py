import logging

from .test_training_common import TestTrainingCommon

class TestSessionSession(TestTrainingCommon):

    def setUp(self):
        super(TestSessionSession, self).setUp()

    def test_session_session(self):
        session_session = self.session_session.search([])
        logging.info('Name :')
        for data in session_session:
            logging.info('   %s' % data.course_id.name)
            logging.info('Start Date : %s' % data.start_date)
            logging.info('End Date : %s' % data.end_date)

            data.check_session_start_date()



class TestCompanyCompany(TestTrainingCommon):

    def setUp(self):
        super(TestCompanyCompany, self).setUp()

    def test_company_company(self):
        self.company01 = self.company_company.create({
            "name":"CompanyTest",
            "phone":14253678954,
            "email":"company@gmail.com"
        })
