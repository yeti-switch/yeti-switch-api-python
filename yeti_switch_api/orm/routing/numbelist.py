from ..base_model import BaseModel, AttributeField


class Numberlist(BaseModel):
    class Meta:
        path = "routing/numberlists"
        type = "numberlists"

    name = AttributeField("name")
    default_action_id = AttributeField("action-id")
    DEFAULT_ACTION_REJECT = 1
    DEFAULT_ACTION_ACCEPT = 2
