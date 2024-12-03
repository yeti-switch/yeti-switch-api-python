from jsonapi_requests.orm import OrmApi

from ..common import build_client_config

from .contractor import Contractor
from .contact import Contact
from .account import Account
from .invoice import Invoice
from .invoice_originated_destination import InvoiceOriginatedDestination
from .invoice_originated_network import InvoiceOriginatedNetwork
from .invoice_terminated_destination import InvoiceTerminatedDestination
from .invoice_terminated_network import InvoiceTerminatedNetwork

from .customers_auth import CustomersAuth
from .dialpeer import Dialpeer
from .numberlist import Numberlist
from .numberlist_item import NumberlistItem
from .rateplan import Rateplan
from .routing_tag import RoutingTag

from .gateway import Gateway
from .gateway_group import GatewayGroup

from .pop import Pop
from .smtp_connection import SmtpConnection
from .country import Country
from .network import Network
from .network_type import NetworkType


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
        cls.__register_model(CustomersAuth)
        cls.__register_model(Dialpeer)
        cls.__register_model(Numberlist)
        cls.__register_model(NumberlistItem)
        cls.__register_model(Rateplan)
        cls.__register_model(RoutingTag)
        cls.__register_model(Gateway)
        cls.__register_model(GatewayGroup)
        cls.__register_model(Pop)
        cls.__register_model(SmtpConnection)
        cls.__register_model(Country)
        cls.__register_model(Network)
        cls.__register_model(NetworkType)

    @classmethod
    def __register_model(cls, model_class):
        cls.api.type_registry.register(model_class)
        model_class._options.api = cls.api
