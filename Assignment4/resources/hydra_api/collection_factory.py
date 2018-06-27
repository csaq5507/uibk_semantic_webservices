import crud
import ctx
import json
import db
from . import hydra
from .supportedClass import HydraClass
from .supportedProperty import HydraProperty
from .supportedOperation import HydraOperation
from .supportedOperation import HydraStatusCode
from . import collection_doc
from flask import Response

myDB = db.db

context_mapping = {}


def generic_entry_get_action(id, entry_context, entry_id, entry_type, db_name):
    result = myDB.get_(db_name, id)
    if type(result) is Response:
        return result
    return ctx.success(result, 200, headers = hydra.LINK_HEADER)

def generic_entry_delete_action(id, entry_context, entry_id, entry_type, db_name):
    result = myDB.delete_(db_name, id)
    if type(result) is Response:
        return result
    return ctx.success(result, 200, headers = hydra.LINK_HEADER)

def generic_entry_replace_action(data, id, entry_context, entry_id, entry_type, db_name):
    current_id = db.next_id()

    entry_url = "{}{}".format(ctx.base_url, entry_id.replace("<id>", current_id))
    data["@context"] = entry_context
    data["@id"] = entry_url
    data["@type"] = entry_type

    result = myDB.replace_(db_name, current_id, data)
    if isinstance(result, Response):
        return result

    headers = hydra.LINK_HEADER
    headers["location"] = entry_url
    headers["content-location"] = entry_url
    return ctx.success(data, 201, headers=headers)

def generic_collection_get_action(collection_context, collection_id, collection_type, db_name):
    result = myDB.getAll_(db_name)
    if type(result) is Response:
        return result

    final_results = []
    for row in result:
        final_results.append( {"@id": row["@id"], "@type": row["@type"]})

    collectionData = {
        "@context": collection_context,
        "@id": collection_id,
        "@type": collection_type,
        "members": final_results
    }
    return ctx.success(collectionData, 200, headers = hydra.LINK_HEADER)

def generic_post_action(data, entry_context, entry_id, entry_type, db_name):
    current_id = db.next_id()

    entry_url = "{}{}".format(ctx.base_url, entry_id.replace("<id>", current_id))
    data["@context"] = entry_context
    data["@id"] = entry_url
    data["@type"] = entry_type

    result = myDB.add_(current_id, db_name, data)
    if isinstance(result, Response):
        return result

    headers = hydra.LINK_HEADER
    headers["location"] = entry_url
    headers["content-location"] = entry_url
    return ctx.success(data, 201, headers=headers)

def post_action(data, operationObj):
    userData = operationObj.hydraClass.userData
    return generic_post_action(
        data,
        userData["entry_@context"],
        userData["entry_@id"],
        userData["entry_@type"],
        userData["entry_@db_name"]
    )

def get_entry_action(id, operationObj):
    userData = operationObj.hydraClass.userData
    return generic_entry_get_action(
        id,
        userData["entry_@context"],
        userData["entry_@id"],
        userData["entry_@type"],
        userData["entry_@db_name"]
    )

def delete_entry_action(id, operationObj):
    userData = operationObj.hydraClass.userData
    return generic_entry_delete_action(
        id,
        userData["entry_@context"],
        userData["entry_@id"],
        userData["entry_@type"],
        userData["entry_@db_name"]
    )

def replace_entry_action(data, id,operationObj):
    userData = operationObj.hydraClass.userData
    return generic_entry_replace_action(
        data,
        id,
        userData["entry_@context"],
        userData["entry_@id"],
        userData["entry_@type"],
        userData["entry_@db_name"]
    )

def get_collection_action(operationObj):
    userData = operationObj.hydraClass.userData
    return generic_collection_get_action(
        userData["collection_@context"],
        userData["collection_@id"],
        userData["collection_@type"],
        userData["entry_@db_name"]
    )


def create_collection_entry(
      type_id = "http://schema.org/Rating"
    , label = "Rating"
    , description = "A rating for a event"
    , hydra_title = "rating"
    , operation_prefix = "rating"
    , end_point = "ratings"
    , properties = []
    , custom_context = None):
    
    context_location = "/api/contexts/{}.jsonld".format(label)

    classObject = HydraClass(
        id=type_id,
        title=label,
        desc = description,
        resource_name = "/api/{}/<id>".format(end_point),
        context_location = context_location
    )

    classObject.userData = {}
    classObject.userData["entry_@context"] = context_location
    classObject.userData["entry_@id"] = "/api/{}/<id>".format(end_point)
    classObject.userData["entry_@db_name"] = end_point
    classObject.userData["entry_@type"] = type_id

    classObject.addOperation(HydraOperation(
        id = "_:{}_retrieve".format(operation_prefix), 
        type = "hydra:Operation", 
        method = "GET", 
        label = "Retrieves an entity", 
        expects = None, 
        returns = type_id,
        operation = get_entry_action
    ))

    classObject.addOperation(HydraOperation(
        id = "_:{}_remove".format(operation_prefix), 
        type = "hydra:Operation", 
        method = "DELETE", 
        label = "Deletes an entity", 
        expects = None, 
        returns = "http://www.w3.org/2002/07/owl#Nothing",
        operation = delete_entry_action
    ))

    classObject.addOperation(HydraOperation(
        id = "_:{}_replace".format(operation_prefix), 
        type = "hydra:Operation", 
        method = "PUT", 
        label = "Replaces an entity", 
        expects = type_id, 
        returns = type_id,
        operation = replace_entry_action
    ))

    classObject.setContextName(label)
  
    for prop in properties:
        classObject.addProperty(prop)

    if not custom_context:
        class_context = { hydra_title: type_id }    
        for prop in properties:
            class_context[prop.data["hydra:title"]] = prop.data["property"]
        classObject.setContext(class_context)
    else:
        classObject.setContext(custom_context)

    hydra.register_class(classObject)
    return classObject


def create_collection(
      type_id = "vocab:RatingCollection"
    , label = "RatingCollection"
    , description = "A collection of ratings"
    , entry_label = "rating"
    , operation_prefix = "rating"
    , end_point = "ratings"
    , entry_point_name = "ratings"
    , entry_context_name = "Rating"
    , expects_type = "http://schema.org/Rating"
    , returns_type = "http://schema.org/Rating"):

    classObject = HydraClass(
        id=type_id,
        title=label,
        subClassOf="http://www.w3.org/ns/hydra/core#Collection",
        desc = "A collection of {}s".format(entry_label),
        resource_name = "/api/{}".format(end_point),
        context_location = "/api/contexts/{}.jsonld".format(label)
    )

    classObject.userData = {}
    classObject.userData["entry_@context"] = "/api/contexts/{}.jsonld".format(entry_context_name)
    classObject.userData["entry_@id"] = "/api/{}/<id>".format(end_point)
    classObject.userData["entry_@db_name"] = end_point
    classObject.userData["entry_@type"] = expects_type

    classObject.userData["collection_@context"] = "/api/contexts/{}.jsonld".format(label)
    classObject.userData["collection_@id"] = "/api/{}/".format(end_point)
    classObject.userData["collection_@db_name"] = end_point
    classObject.userData["collection_@type"] = type_id

    op = HydraOperation(
        id = "_:{}_create".format(operation_prefix), 
        type = "hydra:Operation", 
        method = "POST", 
        label = "Creates a new entry", 
        expects = expects_type,
        returns = returns_type,
        operation = post_action
    )
    op.addStatusCode(HydraStatusCode(201, "If the entry was created successfully."))
    classObject.addOperation(op)

    description_retrieve = "Retrieves all {} entities".format(operation_prefix)
    op = HydraOperation(
        id = "_:{}_collection_retrieve".format(operation_prefix), 
        type = "hydra:Operation", 
        method = "GET", 
        label = "Retrieves all {} entities".format(operation_prefix), 
        expects = None, 
        returns = type_id,
        operation = get_collection_action
    )
    op.addStatusCode(HydraStatusCode(200, "If the all entries are available"))
    classObject.addOperation(op)

    classObject.addProperty(HydraProperty(
            property = "http://www.w3.org/ns/hydra/core#member",
            title ="members",
            desc = "All registered {}".format(operation_prefix),
            required = None,
            readonly = False,
            writeonly = False
    ))

    doc_obj = collection_doc.generate_collection_doc(
        entry_point_name
        , label
        , description
        , description_retrieve
        , operation_prefix
    )

    classObject.setEntryPointName(entry_point_name)
    classObject.setEntryPointDoc(doc_obj)

    classObject.setContextName(label)
    classObject.setContext({
        label: type_id,
        "members": "http://www.w3.org/ns/hydra/core#member"
    })

    hydra.register_class(classObject)
    hydra.add_to_entrypoint(classObject)

    return classObject

