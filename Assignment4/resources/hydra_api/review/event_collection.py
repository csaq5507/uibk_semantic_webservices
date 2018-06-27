from .. import collection_factory
from .. import hydra
from . import actor_collection
from ..supportedProperty import HydraProperty, HydraPropertyInfo

collection_factory.create_collection(
      type_id = "vocab:EventCollection"
    , label = "EventCollection"
    , description = "A collection of events"
    , entry_label = "event"
    , operation_prefix = "event"
    , end_point = "events"
    , entry_point_name = "events"
    , entry_context_name = "Event"
    , expects_type = "http://schema.org/Event"
    , returns_type = "http://schema.org/Event"
)


properties = []
properties.append(HydraProperty(
    title ="name",
    desc = "Name of the event",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "vocab:Issue/name",
        label = "name",
        desc = "Name of the event",
        domain="vocab:Event",
        range="http://www.w3.org/2001/XMLSchema#string"
    )
))


properties.append(HydraProperty(
    title ="actor",
    desc = "The actor for this event",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "vocab:Issue/actor",
        label = "actor",
        desc = "Actor for this event",
        domain="vocab:Event",
        range="vocab:Actor",
        supportedOperations = actor_collection.actor_class.getOperations()
    )
))

properties.append(HydraProperty(
    title ="location",
    desc = "The location where the event takes place",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "vocab:Issue/location",
        label = "location",
        desc = "Location where the event takes place",
        domain="vocab:Event",
        range="vocab:Location"
    )
))

properties.append(HydraProperty(
    title ="description",
    desc = "Event description",
    required = False,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "vocab:Issue/description",
        label = "name",
        desc = "Event description",
        domain="vocab:Event",
        range="http://www.w3.org/2001/XMLSchema#string"
    )
))

properties.append(HydraProperty(
    title ="start_date",
    desc = "Date when the event starts",
    required = False,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "vocab:Issue/start_date",
        label = "start_date",
        desc = "Date when the event starts",
        domain="vocab:Event",
        range="http://www.w3.org/2001/XMLSchema#dateTime"
    )
))

properties.append(HydraProperty(
    title ="end_date",
    desc = "Date when the event ends",
    required = False,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "vocab:Issue/end_date",
        label = "end_date",
        desc = "Date when the event ends",
        domain="vocab:Event",
        range="http://www.w3.org/2001/XMLSchema#dateTime"
    )
))

custom_context = {
    "Event": "http://schema.org/Event",
    "name": "http://schema.org/name",
    "description": "http://schema.org/description",
    "start_date":{
        "@id": "http://schema.org/startDate",
        "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "end_date":{
        "@id": "http://schema.org/endDate",
        "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "location":{
        "@id": "vocab:Event/Location",
        "@type": "@id"
    },
    "actor":{
        "@id": "vocab:Event/actor",
        "@type": "@id"
    }
}

collection_factory.create_collection_entry(
    type_id = "http://schema.org/Event"
    , label = "Event"
    , description = "A collection for a event"
    , hydra_title = "event"
    , operation_prefix = "event"
    , end_point = "events"
    , properties = properties
    , custom_context = custom_context
)