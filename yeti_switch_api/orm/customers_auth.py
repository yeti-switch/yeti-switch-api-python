from .base_model import BaseModel, AttributeField, RelationField


class CustomersAuth(BaseModel):
    class Meta:
        path = "customers-auths"
        type = "customers-auths"

    name = AttributeField("name")
    enabled = AttributeField("enabled")
    reject_calls = AttributeField("reject-calls")

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
    src_number_min_length = AttributeField("src-number-min-length")
    src_number_max_length = AttributeField("src-number-max-length")

    dst_prefix = AttributeField("dst-prefix")
    dst_number_min_length = AttributeField("dst-number-min-length")
    dst_number_max_length = AttributeField("dst-number-max-length")

    x_yeti_auth = AttributeField("x-yeti-auth")

    uri_domain = AttributeField("uri-domain")
    from_domain = AttributeField("from-domain")
    to_domain = AttributeField("to-domain")

    capacity = AttributeField("capacity")
    cps_limit = AttributeField("cps-limit")

    tag_action = RelationField("tag-action")
    tag_action_value = AttributeField("tag-action-value")

    src_rewrite_rule = AttributeField("src-rewrite-rule")
    src_rewrite_result = AttributeField("src-rewrite-result")
    dst_rewrite_rule = AttributeField("dst-rewrite-rule")
    dst_rewrite_result = AttributeField("dst-rewrite-result")


    def creatable_fields(self):
        return [
            "name",
            "enabled",
            "reject-calls",
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
            "src-number-min-length",
            "src-number-max-length",
            "dst-prefix",
            "dst-number-min-length",
            "dst-number-max-length",
            "x-yeti-auth",
            "uri-domain",
            "from-domain",
            "to-domain",
            "capacity",
            "cps-limit",
            "tag-action",
            "tag-action-value",
            "src-rewrite-rule",
            "src-rewrite-result",
            "dst-rewrite-rule",
            "dst-rewrite-result"
        ]

    def updatable_fields(self):
        return self.creatable_fields()
