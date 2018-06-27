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
    , expects_type = "http://schema.org/City"
    , returns_type = "http://schema.org/City"
)

properties = []
properties.append(HydraProperty(
    property = "https://schema.org/name",
    title ="name",
    desc = "Name of the city",
    required = True,
    readonly = False,
    writeonly = False
))
properties.append(HydraProperty(
    property = "http://schema.org/addressCountry",
    title ="addressCountry",
    desc = "The country. For example, USA.",
    required = True,
    readonly = False,
    writeonly = False
))
properties.append(HydraProperty(
    property = "https://schema.org/Population",
    title ="population",
    desc = "City population",
    required = True,
    readonly = False,
    writeonly = False
))
properties.append(HydraProperty(
    property = "https://schema.org/State",
    title ="state",
    desc = "A state or province of a country.",
    required = True,
    readonly = False,
    writeonly = False
))
properties.append(HydraProperty(
    property = "https://schema.org/longitude",
    title ="longitude",
    desc = "Geo coord. latitude longitude",
    required = True,
    readonly = False,
    writeonly = False
))
properties.append(HydraProperty(
    property = "https://schema.org/latitude",
    title ="latitude",
    desc = "Geo coord. latitude",
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