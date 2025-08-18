from .base_model import BaseModel, AttributeField, RelationField

class PackageCounter(BaseModel):
    class Meta:
        path = "package-counters"
        type = "package-counters"

    duration = AttributeField("duration")
    exclude = AttributeField("exclude")
    prefix = AttributeField("prefix")
    service_id = AttributeField("service-id")

    account = RelationField("account")
    service = RelationField("service")
