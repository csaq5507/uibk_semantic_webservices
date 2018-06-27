from .. import collection_factory
from ..supportedProperty import HydraProperty, HydraPropertyInfo

collection_factory.create_collection(
      type_id = "vocab:ActorCollection"
    , label = "ActorCollection"
    , description = "A collection of actors"
    , entry_label = "actor"
    , operation_prefix = "actor"
    , end_point = "actors"
    , entry_point_name = "actors"
    , entry_context_name = "Actor"
    , expects_type = "http://schema.org/Actor"
    , returns_type = "http://schema.org/Actor"
)


properties = []
properties.append(HydraProperty(
        property = "http://schema.org/familyName",
        title ="family_name",
        desc = "The actors's family name",
        required = True,
        readonly = False,
        writeonly = False
))

properties.append(HydraProperty(
        property = "http://schema.org/givenName",
        title ="first_name",
        desc = "The actors's first name",
        required = True,
        readonly = False,
        writeonly = False
))

properties.append(HydraProperty(
        property = "http://schema.org/gender",
        title ="Gender",
        desc = "The actors's gender",
        required = False,
        readonly = False,
        writeonly = False
))

properties.append(HydraProperty(
        property = "http://schema.org/birthDate",
        title ="birthDate",
        desc = "The actors's birth date",
        required = False,
        readonly = False,
        writeonly = False
))

actor_class = collection_factory.create_collection_entry(
    type_id = "http://schema.org/Actor"
    , label = "Actor"
    , description = "A actor for a event"
    , hydra_title = "actor"
    , operation_prefix = "actor"
    , end_point = "actors"
    , properties = properties
)