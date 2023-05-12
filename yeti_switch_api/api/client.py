from jsonapi_requests import Api
from ..common import build_client_config, build_list_kwargs, build_one_kwargs


class Client:
    def __init__(self, config, **kwargs):
        config = build_client_config(config)
        self.api_root = config["API_ROOT"]
        self.auth = config["AUTH"]
        self.api = Api.config(config, **kwargs)

    def get_list(self, resource, **kwargs):
        list_kwargs = build_list_kwargs(**kwargs)
        return self.api.endpoint(resource).get(**list_kwargs)

    def find_by_id(self, resource, id, **kwargs):
        one_kwargs = build_one_kwargs(**kwargs)
        return self.api.endpoint(f"{resource.rstrip('/')}/{id}").get(**one_kwargs)

    def create(self, resource, **kwargs):
        one_kwargs = build_one_kwargs(**kwargs)
        return self.api.endpoint(resource).post(**one_kwargs)

    def update(self, resource, id, **kwargs):
        one_kwargs = build_one_kwargs(**kwargs)
        return self.api.endpoint(f"{resource.rstrip('/')}/{id}").patch(**one_kwargs)

    def delete(self, resource, id, **kwargs):
        return self.api.endpoint(f"{resource.rstrip('/')}/{id}").delete(**kwargs)
