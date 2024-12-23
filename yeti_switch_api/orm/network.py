from .base_model import BaseModel, AttributeField, RelationField  # noqa: F401


class Network(BaseModel):
    class Meta:
        path = "networks"
        type = "networks"

    name = AttributeField("name")
    type = RelationField("network-type")
