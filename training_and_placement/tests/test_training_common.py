from odoo.tests import common


class TestTrainingCommon(common.TransactionCase):
    def setUp(self):
        super(TestTrainingCommon, self).setUp()
        self.applications_applications = self.env['applications.applications']
        self.session_session = self.env['session.session']
        self.company_company = self.env['company.company']

