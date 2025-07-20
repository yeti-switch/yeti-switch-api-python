from yeti_switch_api.orm import PackageCounter, OrmClient

API_ROOT = "http://127.0.0.1:3000/api/rest/admin"
USERNAME = "admin"
PASSWORD = "111111"

config = {
    "API_ROOT": API_ROOT,
    "AUTH_CREDS": {"login": USERNAME, "password": PASSWORD}
}

# Initialize ORM client (registers models)
OrmClient(config)

# Fetch list of package counters
counters = PackageCounter.get_list()
print(f"Total counters: {len(counters)}")
for counter in counters:
    print(f"ID: {counter.id}, Prefix: {counter.prefix}, Duration: {counter.duration}")

# Fetch first counter by ID (if any exist)
if counters:
    first_id = counters[0].id
    counter = PackageCounter.find_by_id(first_id)
    print("\nFirst counter details:")
    print(f"ID: {counter.id}")
    print(f"Attributes: {counter.raw_object.attributes}")
    print(f"Relationships: {counter.raw_object.relationships}")
else:
    print("No package counters found.")
