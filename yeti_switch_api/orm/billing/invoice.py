from ..base_model import BaseModel, AttributeField, RelationField


class Invoice(BaseModel):
    class Meta:
        path = "billing/invoices"
        type = "invoices"

    account = RelationField("account")
    originated_destinations = RelationField("originated-destinations")
    originated_networks = RelationField("originated-networks")
    terminated_destinations = RelationField("terminated-destinations")
    terminated_networks = RelationField("terminated-networks")

    reference = AttributeField("reference")
    state = AttributeField("state")
    invoice_type = AttributeField("invoice-type")
    start_date = AttributeField("start-date")
    end_date = AttributeField("end-date")
    amount_spent = AttributeField("amount-spent")
    amount_earned = AttributeField("amount-earned")

    originated_amount_spent = AttributeField("originated-amount-spent")
    originated_amount_earned = AttributeField("originated-amount-earned")
    originated_calls_count = AttributeField("originated-calls-count")
    originated_successful_calls_count = AttributeField(
        "originated-successful-calls-count"
    )
    originated_calls_duration = AttributeField("originated-calls-duration")
    originated_billing_duration = AttributeField("originated-billing-duration")
    originated_first_call_at = AttributeField("originated-first-call-at")
    originated_last_call_at = AttributeField("originated-last-call-at")

    terminated_amount_spent = AttributeField("terminated-amount-spent")
    terminated_amount_earned = AttributeField("terminated-amount-earned")
    terminated_calls_count = AttributeField("terminated-calls-count")
    terminated_successful_calls_count = AttributeField(
        "terminated-successful-calls-count"
    )
    terminated_calls_duration = AttributeField("terminated-calls-duration")
    terminated_billing_duration = AttributeField("terminated-billing-duration")
    terminated_first_call_at = AttributeField("terminated-first-call-at")
    terminated_last_call_at = AttributeField("terminated-last-call-at")

    def creatable_fields(self):
        return ["account", "start_date", "end_date"]
