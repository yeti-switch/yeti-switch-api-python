from ..base_model import BaseModel, AttributeField, RelationField


class Contact(BaseModel):
    class Meta:
        path = "billing/contacts"
        type = "contacts"

    name = AttributeField("name")
    contractor = RelationField("contractor")
