from ..base_model import BaseModel, AttributeField, RelationField


class CustomersAuth(BaseModel):
    class Meta:
        path = "customers-auths"
        type = "customers-auths"

    name = AttributeField("name")
    src_numberlist = RelationField("src_numberlist")
