from .base_model import BaseModel, AttributeField, RelationField


class Account(BaseModel):
    class Meta:
        path = "accounts"
        type = "accounts"

    contractor = RelationField("contractor")
    timezone = RelationField("timezone")

    external_id = AttributeField("external-id")
    uuid = AttributeField("uuid")

    name = AttributeField("name")
    balance = AttributeField("balance")
    min_balance = AttributeField("min-balance")
    max_balance = AttributeField("max-balance")
    vat = AttributeField("vat")
    balance_low_threshold = AttributeField("balance-low-threshold")
    balance_high_threshold = AttributeField("balance-high-threshold")
    send_balance_notifications_to = AttributeField("send-balance-notifications-to")

    destination_rate_limit = AttributeField("destination-rate-limit")
    max_call_duration = AttributeField("max-call-duration")
    origination_capacity = AttributeField("origination-capacity")
    termination_capacity = AttributeField("termination-capacity")
    total_capacity = AttributeField("total-capacity")

    invoice_template = RelationField("invoice-template")
    invoice_period = AttributeField("invoice-period-id")
    send_invoices_to = AttributeField("send-invoices-to")

    INVOICE_PERIOD_DAILY = 1
    INVOICE_PERIOD_WEEKLY = 2
    INVOICE_PERIOD_BIWEEKLY = 3
    INVOICE_PERIOD_MONTHLY = 4
    INVOICE_PERIOD_BIWEEKLY_SPLIT = 5
    INVOICE_PERIOD_WEEKLY_SPLIT = 6

    def creatable_fields(self):
        return [
            "external-id",
            "uuid",
            "name",
            "contractor",
            "timezone",
            "invoice-template",
            "min-balance",
            "max-balance",
            "vat",
            "balance-low-threshold",
            "balance-high-threshold",
            "send-balance-notifications-to",
            "destination-rate-limit",
            "max-call-duration",
            "origination-capacity",
            "termination-capacity",
            "total-capacity",
            "invoice-period-id",
            "send-invoices-to",
        ]

    def updatable_fields(self):
        return self.creatable_fields()
