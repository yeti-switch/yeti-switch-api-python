from jsonapi_requests.orm import OrmApi

from ..common import build_client_config
from .routing import Rateplan, RoutingTag
from .billing import Contact
from .contractor import Contractor
from .system import SmtpConnection


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
        cls.__register_model(Rateplan)
        cls.__register_model(RoutingTag)
        cls.__register_model(SmtpConnection)

    @classmethod
    def __register_model(cls, model_class):
        cls.api.type_registry.register(model_class)
        model_class._options.api = cls.api
