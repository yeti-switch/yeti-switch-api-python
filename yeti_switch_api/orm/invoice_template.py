from .base_model import BaseModel, AttributeField, RelationField  # noqa: F401


class InvoiceTemplate(BaseModel):
    class Meta:
        path = "invoice-template"
        type = "invoice-template"

    name = AttributeField("name")
    filename = AttributeField("filename")
