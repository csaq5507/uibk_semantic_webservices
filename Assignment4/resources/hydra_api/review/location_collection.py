from .. import collection_factory
from ..supportedProperty import HydraProperty


collection_factory.create_collection(
      type_id = "vocab:LocationCollection"
    , label = "LocationCollection"
    , description = "A collection of locations"
    , entry_label = "location"
    , operation_prefix = "location"
    , end_point = "locations"
    , entry_point_name = "locations"
    , entry_context_name = "Location"
    , expects_type = "http://schema.org/PostalAddress"
    , returns_type = "http://schema.org/PostalAddress"
)


properties = []
properties.append(HydraProperty(
    property = "http://schema.org/addressCountry",
    title ="addressCountry",
    desc = "The country. For example, USA.",
    required = True,
    readonly = False,
    writeonly = False
))
properties.append(HydraProperty(
    property = "http://schema.org/postalCode",
    title ="postalCode",
    desc = "The postal code. For example, 94043.",
    required = True,
    readonly = False,
    writeonly = False
))
properties.append(HydraProperty(
    property = "http://schema.org/streetAddress",
    title ="streetAddress",
    desc = "he street address. For example, 1600 Amphitheatre Pkwy.",
    required = True,
    readonly = False,
    writeonly = False
))

collection_factory.create_collection_entry(
    type_id = "http://schema.org/PostalAddress"
    , label = "Location"
    , description = "A Location for a event"
    , hydra_title = "location"
    , operation_prefix = "location"
    , end_point = "locations"
    , properties = properties
)