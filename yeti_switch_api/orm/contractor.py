from .base_model import BaseModel, AttributeField, RelationField


class Contractor(BaseModel):
    class Meta:
        path = "contractors"
        type = "contractors"

    name = AttributeField("name")
    enabled = AttributeField("enabled")
    vendor = AttributeField("vendor")
    customer = AttributeField("customer")
    description = AttributeField("description")
    address = AttributeField("address")
    phones = AttributeField("phones")
    external_id = AttributeField("external-id")
    smtp_connection = RelationField("smtp-connection")
