from ..base_model import BaseModel, AttributeField, RelationField  # noqa: F401


class NetworkType(BaseModel):
    class Meta:
        path = "system/network-types"
        type = "network-types"

    name = AttributeField("name")
