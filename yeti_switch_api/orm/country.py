from .base_model import BaseModel, AttributeField, RelationField  # noqa: F401


class Country(BaseModel):
    class Meta:
        path = "countries"
        type = "countries"

    name = AttributeField("name")
    host = AttributeField("iso2")
