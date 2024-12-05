from .base_model import BaseModel, AttributeField, RelationField


class Gateway(BaseModel):
    class Meta:
        path = "gateways"
        type = "gateways"

    contractor = RelationField("contractor")
    gateway_group = RelationField("gateway-group")
    pop = RelationField("pop")

    name = AttributeField("name")
    enabled = AttributeField("enabled")
    priority = AttributeField("priority")
    weight = AttributeField("weight")
    allow_origination = AttributeField("allow-origination")
    allow_termination = AttributeField("allow-termination")
    host = AttributeField("host")
    port = AttributeField("port")
    registered_aor_mode = AttributeField("registered-aor-mode-id")

    REGISTERED_AOR_MODE_DISABLE = 1
    REGISTERED_AOR_MODE_AS_IS = 2
    REGISTERED_AOR_MODE_REPLACE_USEPART = 3

    def creatable_fields(self):
        return [
            "contractor",
            "gateway-group",
            "pop",
            "name",
            "enabled",
            "priority",
            "weight",
            "allow-origination",
            "allow-termination",
            "host",
            "port",
            "registered-aor-mode-id",
        ]
