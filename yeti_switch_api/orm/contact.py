from .base_model import BaseModel, AttributeField, RelationField


class Contact(BaseModel):
    class Meta:
        path = "contacts"
        type = "contacts"

    name = AttributeField("name")
    contractor = RelationField("contractor")
