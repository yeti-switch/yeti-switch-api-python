from .base_model import BaseModel, AttributeField, RelationField


class Timezone(BaseModel):
    class Meta:
        path = "timezones"
        type = "timezones"

    name = AttributeField("name")

