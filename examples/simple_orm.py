#!/bin/python3

from yeti_switch_api.orm import OrmClient, Contractor
from yeti_switch_api.orm.billing import Invoice
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
        "API_ROOT": "https://demo.yeti-switch.org/api/rest/admin",
        "AUTH_CREDS": {
            "login": "admin",
            "password": "111111",
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
        "external-id": 100123,
    }
    #    relationships={
    #        "smtp-connection": {
    #            "data": {
    #                "type": SmtpConnection.Meta.type,
    #                "id": found_smtp_connections[0].id,
    #            }
    #        }
    #   },
)
new_contractor.smtp_connection = found_smtp_connections[0]
print("new_contractor before create", new_contractor.raw_object_for_create())
new_contractor.create()
print("new_contractor after create", new_contractor.raw_object)

new_contractor.external_id = 100124
new_contractor.vendor = True
new_contractor.description = "test"
print("new_contractor before update", new_contractor.raw_object_for_update())
new_contractor.update()
print("new_contractor after update", new_contractor.raw_object)

contractor = Contractor.find_by_id(new_contractor.id)
print("contractor found", contractor.raw_object)

print(contractor.creatable_fields())


# get invoices
invs = Invoice.get_list()
if len(invs) == 0:
    print("No invoices found")
else:
    for inv in invs:
        print("Invoices found:", inv.raw_object)
