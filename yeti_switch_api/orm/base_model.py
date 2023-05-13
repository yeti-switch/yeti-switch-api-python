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

    def create(self):
        api_response = self._options.api.endpoint(self.endpoint_path()).post(
            object=self.__raw_object_for_create()
        )
        if api_response.status_code == 201:
            self.raw_object = api_response.content.data

    def update(self):
        api_response = self.endpoint.patch(object=self.__raw_object_for_update())
        if api_response.status_code == 200 and api_response.content.data:
            self.raw_object = api_response.content.data

    def creatable_fields(self):
        return self.__class__._options.fields.keys()

    def updatable_fields(self):
        return self.__class__._options.fields.keys()

    def __raw_object_for_update(self):
        updatable_fields = self.updatable_fields()
        attributes = {
            k: v for k, v in self.raw_object.attributes.items() if k in updatable_fields
        }
        relationships = {
            k: v
            for k, v in self.raw_object.relationships.items()
            if k in updatable_fields
        }
        return JsonApiObject(
            type=self.type,
            id=self.id,
            attributes=attributes,
            relationships=relationships,
        )

    def __raw_object_for_create(self):
        creatable_fields = self.creatable_fields()
        attributes = {
            k: v for k, v in self.raw_object.attributes.items() if k in creatable_fields
        }
        relationships = {
            k: v
            for k, v in self.raw_object.relationships.items()
            if k in creatable_fields
        }
        return JsonApiObject(
            type=self.type,
            attributes=attributes,
            relationships=relationships,
        )
