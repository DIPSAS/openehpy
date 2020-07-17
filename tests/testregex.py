import unittest
from openehpy import client

class Test_regex(unittest.TestCase):

    def test_remove_control_char(self):
        unsanitized = 'abc\r\0\t\n,[]'
        sanitized = 'abc ,[]'
        self.assertEqual(client.server_connection.remove_control_characters(unsanitized),sanitized)

    def test_remove_control_char_from_SQL(self):
        unsanitized = """select
            o/data[at0001]/events[at0006]/time/value as datetime,
            o/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude AS systolic,
            o/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/magnitude AS diastolic
            from
            composition c
            contains observation o[openEHR-EHR-OBSERVATION.blood_pressure.v1]"""
        self.assertFalse('\n' in client.server_connection.remove_control_characters(unsanitized))


    def test_glued_char(self):
        aql = """select
    o/data[at0001]/events[at0006]/time/value as datetime,
    o/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude AS systolic,
    o/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/magnitude AS diastolic
from
    composition c
        contains observation o[openEHR-EHR-OBSERVATION.blood_pressure.v1]
limit 5""" 
        sanitizedAQL = client.server_connection.remove_control_characters(aql)
        self.assertTrue(' from ' in sanitizedAQL)

    def test_removed_unsanitized_string(self):
        aql = """                         select
    o/data[at0001]/events[at0006]/time/value as datetime,
    o/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude AS systolic,
    o/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/magnitude AS diastolic
from                              
    composition c
                                         contains observation o[openEHR-EHR-OBSERVATION.blood_pressure.v1]
limit 5""" 
        sanitizedAQL = client.server_connection.remove_control_characters(aql)
        self.assertTrue('  ' in sanitizedAQL)


if __name__ == '__main__':
    unittest.main()
