import unittest
from openehpy import client

class Test_testPyOpenEHR(unittest.TestCase):

    def setUp(self):
        openEHREndpoint = "https://localhost:4443"
        self.connection = client.server_connection(openEHREndpoint,"utf-8-sig", verifySSLConnection = False)

    def tearDown(self):
        self.connection = ""

    def test_Query_ReturnsResult(self):
        aql = ("SELECT "
        "o/data[at0002]/origin/value AS time,"
        "o/data[at0002]/events[at0003]/data[at0001]/items[at0004]/value/magnitude AS Weight,"
        "o/data[at0002]/events[at0003]/data[at0001]/items[at0004]/value/units AS Unit "
        "FROM COMPOSITION c " 
        "CONTAINS OBSERVATION o[openEHR-EHR-OBSERVATION.body_weight.v1] "
        "ORDER BY o/data[at0002]/origin/value DESC LIMIT 5")
        response = self.connection.query(aql)
        self.assertIsNotNone(response)

    def test_Query_ReturnsResult_with_unsanitized_aql(self):
        aql = ("""                         select
    o/data[at0001]/events[at0006]/time/value as datetime,
    o/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude AS systolic,
    o/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/magnitude AS diastolic
from                              
    composition c
                                         contains observation o[openEHR-EHR-OBSERVATION.blood_pressure.v1]
limit 5""")
        response = self.connection.query(aql)
        self.assertIsNotNone(response)

    def test_Query_ReturnsResult_with_unsanitized_aqlV2(self):
        aql = ("""select
    o/data[at0001]/events[at0006]/time/value as datetime,
    o/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude AS systolic,
    o/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/magnitude AS diastolic
from
    composition c
        contains observation o[openEHR-EHR-OBSERVATION.blood_pressure.v1]
limit 5""")
        response = self.connection.query(aql)
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
