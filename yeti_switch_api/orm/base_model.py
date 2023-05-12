from jsonapi_requests.orm import ApiModel, AttributeField, RelationField  # noqa: F401
from ..common import JsonApiObject, build_list_kwargs


class BaseModel(ApiModel):
    @classmethod
    def find_by_id(cls, id):
        resource = cls.from_id(id)
        resource.refresh()
        return resource

    @classmethod
    def get_list(cls, **kwargs):
        list_kwargs = build_list_kwargs(**kwargs)
        return super(BaseModel, cls).get_list(**list_kwargs)

    @classmethod
    def api_endpoint(cls):
        return cls._options.api.endpoint(cls.endpoint_path())

    @classmethod
    def build(cls, id=None, attributes=None, relationships=None):
        return cls(
            JsonApiObject(
                type=cls.Meta.type,
                id=id,
                attributes=attributes,
                relationships=relationships,
            )
        )
