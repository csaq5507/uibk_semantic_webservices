from .. import collection_factory
from ..supportedProperty import HydraProperty

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
    property = "http://schema.org/ratingValue",
    title ="ratingValue",
    desc = "Rating value",
    required = True,
    readonly = False,
    writeonly = False
))
properties.append(HydraProperty(
    property = "http://schema.org/itemRated",
    title ="itemRated",
    desc = "Event id",
    required = True,
    readonly = False,
    writeonly = False
))
properties.append(HydraProperty(
    property = "http://schema.org/author",
    title ="author",
    desc = "Author id",
    required = True,
    readonly = False,
    writeonly = False
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