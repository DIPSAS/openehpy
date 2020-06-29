import unittest
from openehpy import client

class Test_regex(unittest.TestCase):

    def test_remove_control_char(self):
        unsanitized = 'abc\r\0\t\n,[]'
        sanitized = 'abc,[]'
        self.assertEqual(client.server_connection.remove_control_characters(unsanitized),sanitized)

    def test_remove_control_char_from_SQL(self):
        unsanitized = """select
            o/data[at0001]/events[at0006]/time/value as datetime,
            o/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude AS systolic,
            o/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/magnitude AS diastolic
             from
            composition c
            contains observation o[openEHR-EHR-OBSERVATION.blood_pressure.v1]"""
        sanitized = """select o/data[at0001]/events[at0006]/time/value as datetime, o/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude AS systolic, o/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/magnitude AS diastolic from composition c contains observation o[openEHR-EHR-OBSERVATION.blood_pressure.v1]"""
        test = client.server_connection.remove_control_characters(unsanitized)
        self.assertEqual(client.server_connection.remove_control_characters(unsanitized), sanitized)
if __name__ == '__main__':
    unittest.main()
