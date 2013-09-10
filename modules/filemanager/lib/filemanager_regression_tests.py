# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from invenio.config import CFG_SITE_SECURE_URL
from urllib import urlencode
from invenio.testutils import make_test_suite, run_test_suite, \
    InvenioTestCase, test_web_page_content, test_web_page_existence

class FileManagerRegressionTests(InvenioTestCase):

    def setUp(self):
        self.csv_file = CFG_SITE_SECURE_URL + '/static/test.csv'

    def test_no_valid_action(self):
        params = [('action', 'anything')]
        url = CFG_SITE_SECURE_URL + '/filemanager?' + urlencode(params)
        errors  = test_web_page_content(url)
        print errors
        assert 'HTTP Error 406' in errors[0]

    def test_join_files(self):
        params = [('action', 'join'), ('file', self.csv_file), ('file', self.csv_file)]
        url = (CFG_SITE_SECURE_URL + '/filemanager?' + urlencode(params))
        test_web_page_existence(url)
        expected =('London Borough of Hammersmith and Fulham,2010-01-01,483559,GBP,2950'
                   ',e-MENTORING LIMITED,Childrens Services,29\nLondon Borough of Hammer'
                   'smith and Fulham,2010-01-01,405869,GBP,898.64,ADT FIRE & SECURITY PLC'
                   ',Childrens Services,1')

        errors  = test_web_page_content(url, expected_text=expected)
        self.assertEquals([], errors)

    def test_csv_to_json_files(self):
        params = [('action', 'csvtojson'), ('file', self.csv_file)]
        url = (CFG_SITE_SECURE_URL + '/filemanager?' + urlencode(params))
        test_web_page_existence(url)
        expected = ('"paid_to": "EDF ENERGY 1 LIMITED", "currency": "GBP", "'
                    'amount": "-1156.27", "date": "2010-01-01", "paid_by": "London '
                    'Borough of Hammersmith and Fulham", "transaction_id": "409318"},'
                    ' {"unique_rowid": "28", "spending_area": "Resident Services", "paid_to"'
                    ': "EDF ENERGY 1 LIMITED", "currency": "GBP", "amount": "-826.32", "date"'
                    ': "2010-01-01", "paid_by": "London Borough of Hammersmith and Fulham", '
                    '"transaction_id": "409319"}, {"unique_rowid": "29", "spending_area": "Ch'
                    'ildrens Services", "paid_to": "e-MENTORING LIMITED", "currency": "GBP", '
                    '"amount": "2950", "date": "2010-01-01", "paid_by": "London Borough of '
                    'Hammersmith and Fulham", "transaction_id": "483559"}]')
        errors  = test_web_page_content(url, expected_text=expected)
        self.assertEquals([], errors)

    def test_cut_files(self):
        params = [('action', 'cut'), ('file', self.csv_file), ('field', 'paid_by'),
                                                              ('field', 'amount'),
                                                              ('field', 'spending_area')]
        url = (CFG_SITE_SECURE_URL + '/filemanager?' + urlencode(params))
        test_web_page_existence(url)
        expected = ('paid_by,amount,spending_area\nLondon Borough of Hammers'
                    'mith and Fulham,898.64,Childrens Services\nLondon Boroug'
                    'h of Hammersmith and Fulham,517.85,Resident Services\nLon'
                    'don Borough of Hammersmith and Fulham,1215.97,Regeneration'
                    ' and Housing Services')
        errors  = test_web_page_content(url, expected_text=expected)
        self.assertEquals([], errors)

TEST_SUITE = make_test_suite(FileManagerRegressionTests)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE)
