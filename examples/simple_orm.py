#!/bin/python3

from yeti_switch_api.orm import OrmClient
from yeti_switch_api.orm import Contractor
from yeti_switch_api.orm.system import SmtpConnection

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

# here library usage starts
OrmClient(
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

# refresh auth token in any time
OrmClient.auth.refresh_token()

found_smtp_connections = SmtpConnection.get_list()
found_contractors = Contractor.get_list(
    filter={"name_eq": "test_python"}, page_number=1
)

if len(found_contractors) == 0:
    print("old_contractor not found")
else:
    old_contractor = found_contractors[0]
    print("old_contractor found", old_contractor.raw_object)
    old_contractor.delete()
    print("old_contractor deleted")

new_contractor = Contractor.build(
    attributes={
        "name": "test_python",
        "enabled": True,
        "customer": True,
    },
    relationships={
        "smtp-connection": {
            "data": {
                "type": SmtpConnection.Meta.type,
                "id": found_smtp_connections[0].id,
            }
        }
    },
)
print("new_contractor before create", new_contractor.raw_object)
new_contractor.create()
print("new_contractor after create", new_contractor.raw_object)
