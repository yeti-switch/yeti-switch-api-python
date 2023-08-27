from ..base_model import BaseModel, AttributeField, RelationField


class NumberlistItem(BaseModel):
    class Meta:
        path = "routing/numberlist-items"
        type = "numberlist-items"

    key = AttributeField("key")
    number_min_length = AttributeField("number_min_length")
    number_max_length = AttributeField("number_max_length")
    src_rewrite_rule = AttributeField("src_rewrite_rule")
    src_rewrite_result = AttributeField("src_rewrite_result")
    dst_rewrite_rule = AttributeField("dst_rewrite_rule")
    dst_rewrite_result = AttributeField("dst_rewrite_result")
    created_at = AttributeField("created_at")
    updated_at = AttributeField("updated_at")
    numberlist = RelationField("numberlist")
    action_id = AttributeField("action-id")
    ACTION_REJECT = 1
    ACTION_ACCEPT = 2
