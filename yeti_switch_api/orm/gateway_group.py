from .base_model import BaseModel, AttributeField, RelationField


class GatewayGroup(BaseModel):
    class Meta:
        path = "gateway-groups"
        type = "gateway-groups"

    vendor = RelationField("vendor")

    name = AttributeField("name")
