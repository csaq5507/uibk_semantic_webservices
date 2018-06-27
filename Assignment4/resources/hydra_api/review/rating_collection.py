from .. import collection_factory
from ..supportedProperty import HydraProperty, HydraPropertyInfo

collection_factory.create_collection(
      type_id = "vocab:RatingCollection"
    , label = "RatingCollection"
    , description = "A collection of ratings"
    , entry_label = "rating"
    , operation_prefix = "rating"
    , end_point = "ratings"
    , entry_point_name = "ratings"
    , entry_context_name = "Rating"
    , expects_type = "http://schema.org/Rating"
    , returns_type = "http://schema.org/Rating"
)


properties = []
properties.append(HydraProperty(
    title ="ratingValue",
    desc = "Rating value",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "http://schema.org/ratingValue"
    )
))
properties.append(HydraProperty(
    title ="itemRated",
    desc = "Event id",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "http://schema.org/itemRated"
    )
))
properties.append(HydraProperty(
    title ="author",
    desc = "Author id",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "http://schema.org/author"
    )
))

custom_context = {
    "Rating": "http://schema.org/Rating",
    "itemRated": "http://schema.org/itemRated",
    "ratingValue": "http://schema.org/ratingValue",
    "author":{
        "@id": "vocab:Rating/author",
        "@type": "@id"
    }
}

collection_factory.create_collection_entry(
    type_id = "http://schema.org/Rating"
    , label = "Rating"
    , description = "A rating for a event"
    , hydra_title = "rating"
    , operation_prefix = "rating"
    , end_point = "ratings"
    , properties = properties
    , custom_context = custom_context
)