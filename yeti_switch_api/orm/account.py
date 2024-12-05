from .base_model import BaseModel, AttributeField, RelationField


class Account(BaseModel):
    class Meta:
        path = "accounts"
        type = "account"

    contractor = RelationField("contractor")

    name = AttributeField("name")
    balance = AttributeField("balance")
    min_balance = AttributeField("min-balance")
    max_balance = AttributeField("max-balance")

    def creatable_fields(self):
        return ["contractor", "min_balace", "max_balance"]
