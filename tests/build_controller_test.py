import unittest

from starlette.testclient import TestClient

from tests import load_test_file
from tests.test_base import get_test_client, truncate_db


class MyTestCase(unittest.TestCase):
    client: TestClient

    @classmethod
    def setUpClass(cls):
        cls.client = get_test_client()

    @classmethod
    def tearDownClass(cls):
        truncate_db()
        print("Teardown after tests")

    def test_insert_valid_build_then_retrieve(self):
        """
        GIVEN: valid build xml that can be parsed
        WHEN: receiving the data
        THEN: return a 200 and a key to look up the data
        """
        build_xml = load_test_file("resources/test_build.xml")
        response = self.client.post('/pastes', build_xml, headers={'Content-Type': 'application/xml'})
        response_json = response.json()

        self.assertEqual(200, response.status_code)
        expected_key = 'pKmOPLok'
        self.assertEqual(expected_key, response_json['key'])

        # basic get
        response = self.client.get(f"/pastes/{expected_key}")
        response_json = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual(build_xml, response_json['raw_xml'])

    def test_insert_valid_build_then_retrieve_raw(self):
        """
        GIVEN: valid build xml that can be parsed
        WHEN: receiving the data
        THEN: return a 200 and a key to look up the raw data
        """
        build_xml = load_test_file("resources/test_build.xml")
        response = self.client.post('/pastes', build_xml, headers={'Content-Type': 'application/xml'})
        response_json = response.json()

        self.assertEqual(200, response.status_code)
        expected_key = 'pKmOPLok'
        self.assertEqual(expected_key, response_json['key'])

        # raw get
        response = self.client.get(f"/pastes/{expected_key}/raw")
        self.assertEqual(200, response.status_code)
        self.assertEqual(build_xml, response.text)

    def test_insert_invalid_build(self):
        """
        GIVEN: malformed build xml that cant be parsed
        WHEN: receiving the data
        THEN: return a 400 error and the message "No valid build XML"
        """
        build_xml = load_test_file("resources/malformed_build_items_missing.xml")
        response = self.client.post('/pastes', build_xml, headers={'Content-Type': 'application/xml'})
        response_json = response.json()
        print(response, response_json)
        self.assertEqual(400, response.status_code)
        self.assertEqual("No valid build XML.", response_json)


if __name__ == '__main__':
    unittest.main()
