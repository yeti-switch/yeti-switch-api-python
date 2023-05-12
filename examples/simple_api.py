#!/bin/python3
from yeti_switch_api.api import Client
from yeti_switch_api.common import JsonApiObject

# For demonstration purpose only: below lines logs all HTTP requests to stdout
#
# import logging
# import http.client
#
# http.client.HTTPConnection.debuglevel = 1
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

client = Client(
    {
        "API_ROOT": "http://127.0.0.1:4321/api/rest/admin",
        "AUTH_CREDS": {
            "login": "admin",
            "password": "qweasd",
        },
        "VALIDATE_SSL": True,
        "TIMEOUT": 1,
    }
)

client.auth.refresh_token()

found_contractors = client.get_list(
    "contractors", filter={"name_eq": "test_python"}, page_size=1
)
found_smtp_connections = client.get_list("system/smtp-connections")

if len(found_contractors.data) == 0:
    print("old_contractor not found")
else:
    old_contractor = found_contractors.data[0]
    print("old_contractor found", old_contractor)
    client.delete("contractors", old_contractor.id)
    print("old_contractor deleted")

create_response = client.create(
    "contractors",
    object=JsonApiObject(
        type="contractors",
        attributes={
            "name": "test_python",
            "enabled": True,
            "customer": True,
        },
        relationships={
            "smtp-connection": {
                "data": {
                    "type": found_smtp_connections.data[0].type,
                    "id": found_smtp_connections.data[0].id,
                }
            }
        },
    ),
)

new_contractor = create_response.content
print("new_contractor", new_contractor)
