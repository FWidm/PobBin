from fastapi.logger import logger
from lxml import etree

from pobbin import load_file_as_string

XSD_PATH = "assets/pob_build.xsd"
XSD_CONTENT = load_file_as_string(XSD_PATH)


def is_valid_pob(pob_build_xml: str) -> bool:
    schema_doc = etree.XML(XSD_CONTENT)
    schema = etree.XMLSchema(schema_doc)
    parser = etree.XMLParser(schema=schema)
    try:
        etree.XML(pob_build_xml, parser)
    except etree.XMLSyntaxError as e:
        logger.warning(f"Incoming build does not match DTD: '{e}'")
        return False
    return True
