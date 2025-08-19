from .base_model import BaseModel, AttributeField, RelationField


class Numberlist(BaseModel):
    class Meta:
        path = "numberlists"
        type = "numberlists"

    external_id = AttributeField("external-id")
    external_type = AttributeField("external-type")

    name = AttributeField("name")
    default_action = AttributeField("default-action-id")
    DEFAULT_ACTION_REJECT = 1
    DEFAULT_ACTION_ACCEPT = 2

    mode = AttributeField("mode-id")
    MODE_STRICT = 1
    MODE_PREFIX = 2
    MODE_RANDOM = 3

    default_src_rewrite_rule = AttributeField("default-src-rewrite-rule")
    default_src_rewrite_result = AttributeField("default-src-rewrite-result")
    defer_src_rewrite = AttributeField("defer-src-rewrite")
    default_dst_rewrite_rule = AttributeField("default-dst-rewrite-rule")
    default_dst_rewrite_result = AttributeField("default-dst-rewrite-result")
    defer_dst_rewrite = AttributeField("defer-dst-rewrite")

    tag_action = RelationField("tag-action")
    tag_action_value = AttributeField("tag-action-value")

    created_at = AttributeField("created-at")
    updated_at = AttributeField("updated-at")

    def creatable_fields(self):
        return [
            "name",
            "default-action-id",
            "tag-action",
            "tag-action-value",
            "mode-id",
            "default-src-rewrite-rule",
            "default-src-rewrite-result",
            "defer-src-rewrite",
            "default-dst-rewrite-rule",
            "default-dst-rewrite-result",
            "defer-dst-rewrite",
            "external-id",
            "external-type",
        ]

    def updatable_fields(self):
        return self.creatable_fields()
