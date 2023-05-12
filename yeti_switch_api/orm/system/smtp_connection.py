from ..base_model import BaseModel, AttributeField, RelationField  # noqa: F401


class SmtpConnection(BaseModel):
    class Meta:
        path = "system/smtp-connections"
        type = "smtp-connections"

    name = AttributeField("name")
    host = AttributeField("host")
    port = AttributeField("port")
    from_address = AttributeField("from-address")
    auth_user = AttributeField("auth-user")
    auth_password = AttributeField("auth-password")
    is_global = AttributeField("global")
