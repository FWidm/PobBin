import unittest

from pobbin.util.pob_xml_verifier import is_valid_pob
from tests import load_file_as_bytes


class TestXmlVerifier(unittest.TestCase):
    def test_empty_build(self):
        xml_string = load_file_as_bytes("tests/resources/empty_build.xml")
        valid_pob = is_valid_pob(xml_string)
        self.assertTrue(valid_pob, "Empty build should always be parsed as valid.")

    def test_ziz_build(self):
        xml_string = load_file_as_bytes("tests/resources/ziz_huge_build.xml")
        valid_pob = is_valid_pob(xml_string)
        self.assertTrue(valid_pob, "Full blown build should be parsed as valid.")

    def test_malformed_build_with_missing_items(self):
        xml_string = load_file_as_bytes("tests/resources/malformed_build_items_missing.xml")
        valid_pob = is_valid_pob(xml_string)
        self.assertFalse(valid_pob, "Malformed build should always be parsed as invalid.")


if __name__ == '__main__':
    unittest.main()
