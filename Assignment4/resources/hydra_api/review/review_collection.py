from .. import collection_factory
from ..supportedProperty import HydraProperty, HydraPropertyInfo

collection_factory.create_collection(
      type_id = "vocab:ReviewCollection"
    , label = "ReviewCollection"
    , description = "A collection of reviews"
    , entry_label = "review"
    , operation_prefix = "review"
    , end_point = "reviews"
    , entry_point_name = "reviews"
    , entry_context_name = "Review"
    , expects_type = "http://schema.org/Review"
    , returns_type = "http://schema.org/Review"
)


properties = []
properties.append(HydraProperty(
    title ="reviewBody",
    desc = "Review content",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "http://schema.org/reviewBody"
    )
))
properties.append(HydraProperty(
    title ="itemReviewed",
    desc = "Event id",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "http://schema.org/itemReviewed"
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
    "Review": "http://schema.org/Review",
    "itemReviewed": "http://schema.org/itemReviewed",
    "reviewBody": "http://schema.org/reviewBody",
    "author":{
        "@id": "vocab:Rating/author",
        "@type": "@id"
    }
}

collection_factory.create_collection_entry(
    type_id = "http://schema.org/Review"
    , label = "Review"
    , description = "A review for a event"
    , hydra_title = "review"
    , operation_prefix = "review"
    , end_point = "reviews"
    , properties = properties
    , custom_context = custom_context
)