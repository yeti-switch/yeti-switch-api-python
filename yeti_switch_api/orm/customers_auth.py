from .base_model import BaseModel, AttributeField, RelationField


class CustomersAuth(BaseModel):
    class Meta:
        path = "customers-auths"
        type = "customers-auths"

    name = AttributeField("name")
    enabled = AttributeField("enabled")
    src_numberlist = RelationField("src-numberlist")
    dst_numberlist = RelationField("dst-numberlist")
    customer = RelationField("customer")
    account = RelationField("account")
    rateplan = RelationField("rateplan")
    routing_plan = RelationField("routing-plan")
    gateway = RelationField("gateway")
    pop = RelationField("pop")
    ip = AttributeField("ip")
    src_prefix = AttributeField("src-prefix")
    dst_prefix = AttributeField("dst-prefix")
    x_yeti_auth = AttributeField("x-yeti-auth")

    def creatable_fields(self):
        return [
            "name",
            "enabled",
            "src-numberlist",
            "dst-numberlist",
            "customer",
            "account",
            "rateplan",
            "routing-plan",
            "gateway",
            "pop",
            "ip",
            "src-prefix",
            "dst-prefix",
            "x-yeti-auth",
        ]
