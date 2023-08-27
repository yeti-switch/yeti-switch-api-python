from ..base_model import BaseModel, AttributeField


class Dialpeer(BaseModel):
    class Meta:
        path = "dialpeers"
        type = "dialpeers"

    enabled = AttributeField("enabled")
    next_rate = AttributeField("next-rate")
    connect_fee = AttributeField("connect-fee")
    initial_rate = AttributeField("initial-rate")
    initial_interval = AttributeField("initial-interval")
    next_interval = AttributeField("next-interval")
    valid_from = AttributeField("valid-from")
    valid_till = AttributeField("valid-till")
    prefix = AttributeField("prefix")
    src_rewrite_rule = AttributeField("src-rewrite-rule")
    dst_rewrite_rule = AttributeField("dst-rewrite-rule")
    acd_limit = AttributeField("acd-limit")
    asr_limit = AttributeField("asr-limit")
    src_rewrite_result = AttributeField("src-rewrite-result")
    dst_rewrite_result = AttributeField("dst-rewrite-result")
    locked = AttributeField("locked")
    priority = AttributeField("priority")
    exclusive_route = AttributeField("exclusive-route")
    capacity = AttributeField("capacity")
    lcr_rate_multiplier = AttributeField("lcr-rate-multiplier")
    force_hit_rate = AttributeField("force-hit-rate")
    network_prefix_id = AttributeField("network-prefix-id")
    created_at = AttributeField("created-at")
    short_calls_limit = AttributeField("short-calls-limit")
    external_id = AttributeField("external-id")
    routing_tag_ids = AttributeField("routing-tag-ids")
    dst_number_min_length = AttributeField("dst-number-min-length")
    dst_number_max_length = AttributeField("dst-number-max-length")
    reverse_billing = AttributeField("reverse-billing")
