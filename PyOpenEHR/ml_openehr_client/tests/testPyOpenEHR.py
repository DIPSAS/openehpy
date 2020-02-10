import unittest
import ml_openehr_client.PyOpenEHR as PyOpenEHR

class Test_testPyOpenEHR(unittest.TestCase):

    def setUp(self):
        self.connection = PyOpenEHR.PyOpenEHR("https://vt-selecta-srv3:4443", "utf-8-sig", False)

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
        response = self.connection.query(aql);
        self.assertEquals("RESULTSET", response["_type"])

if __name__ == '__main__':
    unittest.main()
