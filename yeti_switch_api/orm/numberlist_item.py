from .base_model import BaseModel, AttributeField, RelationField


class NumberlistItem(BaseModel):
    class Meta:
        path = "numberlist-items"
        type = "numberlist-items"

    numberlist = RelationField("numberlist")
    key = AttributeField("key")
    number_min_length = AttributeField("number-min-length")
    number_max_length = AttributeField("number-max-length")
    src_rewrite_rule = AttributeField("src-rewrite-rule")
    src_rewrite_result = AttributeField("src-rewrite-result")
    defer_src_rewrite = AttributeField("defer-src-rewrite")

    dst_rewrite_rule = AttributeField("dst-rewrite-rule")
    dst_rewrite_result = AttributeField("dst-rewrite-result")
    defer_dst_rewrite = AttributeField("defer-dst-rewrite")

    created_at = AttributeField("created-at")
    updated_at = AttributeField("updated-at")

    action_id = AttributeField("action-id")
    ACTION_REJECT = 1
    ACTION_ACCEPT = 2

    tag_action = RelationField("tag-action")
    tag_action_value = AttributeField("tag-action-value")

    def creatable_fields(self):
        return [
            "numberlist"
            "key",
            "number-min-length",
            "number-max-length",
            "src-rewrite-rule",
            "src-rewrite-result",
            "defer-src-rewrite"
            "dst-rewrite-rule",
            "dst-rewrite-result",
            "defer-dst-rewrite",
            "action-id",
            "tag-action",
            "tag-action-value"
        ]

    def updatable_fields(self):
        return self.creatable_fields()
