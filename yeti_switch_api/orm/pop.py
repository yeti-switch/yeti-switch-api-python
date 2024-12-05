from .base_model import BaseModel, AttributeField, RelationField  # noqa: F401


class Pop(BaseModel):
    class Meta:
        path = "pops"
        type = "pops"

    name = AttributeField("name")
