def paste_xml_request_body_override(openapi_schema):
    """
    @TODO: this is very ugly, but it works. It should really be easier to make this work -_-
    right now this just replaces the /pastes "post" endpoint documentation and we pretend
    it accepts xml
    """
    openapi_schema["paths"]["/pastes"]["post"]["requestBody"] = {
        "content": {
            "application/xml": {
                "schema": {
                    "title": "Paste",
                    "type": "string"
                }
            }
        },
        "required": True
    }
