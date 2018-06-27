from .. import collection_factory
from ..supportedProperty import HydraProperty, HydraPropertyInfo


collection_factory.create_collection(
      type_id = "vocab:LocationCollection"
    , label = "LocationCollection"
    , description = "A collection of locations"
    , entry_label = "location"
    , operation_prefix = "location"
    , end_point = "locations"
    , entry_point_name = "locations"
    , entry_context_name = "Location"
    , expects_type = "http://schema.org/City"
    , returns_type = "http://schema.org/City"
)

properties = []
properties.append(HydraProperty(
    title ="name",
    desc = "Name of the city",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "http://schema.org/name"
    )
))
properties.append(HydraProperty(
    title ="addressCountry",
    desc = "The country. For example, USA.",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "http://schema.org/addressCountry"
    )
))
properties.append(HydraProperty(
    title ="population",
    desc = "City population",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "http://schema.org/population"
    )
))
properties.append(HydraProperty(
    title ="state",
    desc = "A state or province of a country.",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "http://schema.org/State"
    )
))
properties.append(HydraProperty(
    title ="longitude",
    desc = "Geo coord. latitude longitude",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "http://schema.org/longitude"
    )
))
properties.append(HydraProperty(
    title ="latitude",
    desc = "Geo coord. latitude",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "http://schema.org/latitude"
    )
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