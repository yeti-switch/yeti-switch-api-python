from .auth import Auth
from jsonapi_requests import JsonApiObject  # noqa: F401


def build_client_config(config):
    config = config.copy()
    if "AUTH_CREDS" in config:
        auth_creds = config.pop("AUTH_CREDS")
        login = auth_creds["login"]
        password = auth_creds["password"]
        config["AUTH"] = Auth(login=login, password=password, url=config["API_ROOT"])

    return config


def build_list_kwargs(**kwargs):
    result = kwargs.copy()
    params = kwargs["params"].copy() if "params" in kwargs else {}

    __build_include_param(result=result, params=params)

    filters = result.pop("filter") if "filter" in result else None
    if filters is not None:
        for name, value in filters.items():
            params[f"filter[{name}]"] = value

    sort = result.pop("sort") if "sort" in result else None
    if sort is not None:
        params["sort"] = sort

    page_number = result.pop("page_number") if "page_number" in result else None
    if page_number is not None:
        params["page[number]"] = page_number

    page_size = result.pop("page_size") if "page_size" in result else None
    if page_size is not None:
        params["page[size]"] = page_size

    if len(params.keys()) > 0:
        result["params"] = params
    return result


def build_one_kwargs(**kwargs):
    result = kwargs.copy()
    params = kwargs["params"].copy() if "params" in kwargs else {}

    __build_include_param(result=result, params=params)

    result["params"] = params
    return result


def __build_include_param(result, params):
    include = result.pop("include") if "include" in result else None
    if include is not None:
        params["include"] = include if isinstance(include, list) else [include]
