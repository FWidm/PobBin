from fastapi.logger import logger as fastapi_logger

from lxml import etree

from pobbin import load_file_as_string


class XsdVerifier:

    def __init__(self, xsd_path="assets/pob_build.xsd"):
        self.xsd_content = load_file_as_string(xsd_path)

    def is_valid_pob(self, pob_build_xml: str) -> bool:
        schema_doc = etree.XML(self.xsd_content)
        schema = etree.XMLSchema(schema_doc)
        parser = etree.XMLParser(schema=schema)
        try:
            etree.XML(pob_build_xml, parser)
        except etree.XMLSyntaxError as e:
            fastapi_logger.warning(f"Incoming build does not match DTD: '{e}'")
            return False
        return True


xsd_verifier = XsdVerifier()
