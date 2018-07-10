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
        id = "vocab:Rating/ratingValue",
        label = "ratingValue",
        desc = "Rating value of the event",
        domain="vocab:Rating",
        range="http://www.w3.org/2001/XMLSchema#positiveInteger"
    )
))
properties.append(HydraProperty(
    title ="itemRated",
    desc = "Event id",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "vocab:Rating/itemRated",
        label = "ratingValue",
        desc = "Rated event",
        domain="vocab:Rating",
        range="vocab:Event"
    )
))
properties.append(HydraProperty(
    title ="author",
    desc = "Author id",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "vocab:Rating/author",
        label = "author",
        desc = "Auhtor for this rating",
        domain="vocab:Rating",
        range="http://www.w3.org/2001/XMLSchema#string"
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