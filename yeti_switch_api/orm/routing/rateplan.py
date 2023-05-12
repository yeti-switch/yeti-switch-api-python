from ..base_model import BaseModel, AttributeField


class Rateplan(BaseModel):
    class Meta:
        path = "routing/rateplans"
        type = "rateplans"

    name = AttributeField("name")
    profit_control_mode_id = AttributeField("profit-control-mode-id")
