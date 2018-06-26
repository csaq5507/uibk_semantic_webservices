from .. import collection_factory
from .. import hydra
from ..supportedProperty import HydraProperty

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
        property = "http://schema.org/name",
        title ="name",
        desc = "Name of the event",
        required = True,
        readonly = False,
        writeonly = False
))
properties.append(HydraProperty(
        property = "http://schema.org/actor",
        title ="actor",
        desc = "The actor for this event",
        required = True,
        readonly = False,
        writeonly = False
))

properties.append(HydraProperty(
        property = "http://schema.org/PostalAddress",
        title ="location",
        desc = "The location where the event takes place",
        required = True,
        readonly = False,
        writeonly = False
))

properties.append(HydraProperty(
        property = "https://schema.org/description",
        title ="description",
        desc = "Event description",
        required = False,
        readonly = False,
        writeonly = False
))

properties.append(HydraProperty(
        property = "https://schema.org/startDate",
        title ="start_date",
        desc = "Date when the event starts",
        required = False,
        readonly = False,
        writeonly = False
))

properties.append(HydraProperty(
        property = "https://schema.org/startDate",
        title ="end_date",
        desc = "Date when the event ends",
        required = False,
        readonly = False,
        writeonly = False
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
    , description = "A event for a event"
    , hydra_title = "event"
    , operation_prefix = "event"
    , end_point = "events"
    , properties = properties
    , custom_context = custom_context
)