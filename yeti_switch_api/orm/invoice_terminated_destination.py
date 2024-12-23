from .base_model import BaseModel, AttributeField, RelationField


class InvoiceTerminatedDestination(BaseModel):
    class Meta:
        path = "invoice-terminated-destinations"
        type = "invoice-terminated-destinations"

    invoice = RelationField("invoice")
    country = RelationField("country")
    network = RelationField("network")

    amount = AttributeField("amount")
    billing_duration = AttributeField("billing-duration")
    calls_count = AttributeField("calls-count")
    successful_calls_count = AttributeField("successful-calls-count")
    calls_duration = AttributeField("calls-duration")
    dst_prefix = AttributeField("dst-prefix")
    first_call_at = AttributeField("first-call-at")
    last_call_at = AttributeField("last-call-at")
    rate = AttributeField("rate")
    spent = AttributeField("spent")
