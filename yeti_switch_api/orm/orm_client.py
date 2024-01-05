from jsonapi_requests.orm import OrmApi

from ..common import build_client_config
from .routing import Rateplan, RoutingTag
from .billing import (
    Contact,
    Account,
    Invoice,
    InvoiceOriginatedDestination,
    InvoiceOriginatedNetwork,
    InvoiceTerminatedDestination,
    InvoiceTerminatedNetwork,
)
from .contractor import Contractor
from .equipment import Gateway, GatewayGroup
from .system import SmtpConnection, Country, Network, NetworkType


class OrmClient:
    api_root = None
    auth = None
    api = None

    def __new__(cls, config, **kwargs):
        config = build_client_config(config)
        cls.api_root = config["API_ROOT"]
        cls.auth = config["AUTH"]
        cls.api = OrmApi.config(config, **kwargs)
        cls.__register_models()

    @classmethod
    def __register_models(cls):
        cls.__register_model(Contractor)
        cls.__register_model(Contact)
        cls.__register_model(Account)
        cls.__register_model(Invoice)
        cls.__register_model(InvoiceOriginatedDestination)
        cls.__register_model(InvoiceOriginatedNetwork)
        cls.__register_model(InvoiceTerminatedDestination)
        cls.__register_model(InvoiceTerminatedNetwork)
        cls.__register_model(Gateway)
        cls.__register_model(GatewayGroup)
        cls.__register_model(Country)
        cls.__register_model(Network)
        cls.__register_model(NetworkType)
        cls.__register_model(Rateplan)
        cls.__register_model(RoutingTag)
        cls.__register_model(SmtpConnection)

    @classmethod
    def __register_model(cls, model_class):
        cls.api.type_registry.register(model_class)
        model_class._options.api = cls.api
