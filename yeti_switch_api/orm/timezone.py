from .base_model import BaseModel, AttributeField


class Timezone(BaseModel):
    class Meta:
        path = "timezones"
        type = "timezones"

    name = AttributeField("name")
