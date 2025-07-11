from .base_model import BaseModel, AttributeField


class RoutingPlan(BaseModel):
    class Meta:
        path = "routing-plans"
        type = "routing-plans"

    name = AttributeField("name")
    rate_delta_max = AttributeField("rate-delta-max")
    use_lnp = AttributeField("use-lnp")
    max_rerouting_attempts = AttributeField("max-rerouting-attempts")
