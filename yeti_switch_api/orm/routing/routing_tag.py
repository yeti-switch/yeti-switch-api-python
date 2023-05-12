from ..base_model import BaseModel, AttributeField


class RoutingTag(BaseModel):
    class Meta:
        path = "routing/routing-tags"
        type = "routing-tags"

    name = AttributeField("name")
