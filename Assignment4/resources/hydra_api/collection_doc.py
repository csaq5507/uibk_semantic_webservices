
def make_get(name, type_name):
    return {
        "@id": "_:{}_retrieve".format(name),
        "@type": "hydra:Operation",
        "method": "GET",
        "label": "Retrieves a Event entity",
        "description": null,
        "expects": null,
        "returns": type_name,
        "statusCodes": []
    }
    
def make_put(name, type_name):
    return  {
        "@id": "_:{}_replace".format(name),
        "@type": "http://schema.org/UpdateAction",
        "method": "PUT",
        "label": "Replaces an existing entity",
        "description": null,
        "expects": type_name,
        "returns": type_name,
        "statusCodes": [
            {
            "code": 404,
            "description": "If the entity wasn't found."
            }
        ]
    }


def make_patch(name, type_name):
    return {
        "@id": "_:{}_patch".format(name),
        "@type": "http://schema.org/UpdateAction",
        "method": "PATCH",
        "label": "Updates some fields an existing entity",
        "description": null,
        "expects": type_name,
        "returns": type_name,
        "statusCodes": [
            {
            "code": 404,
            "description": "If the entity wasn't found."
            },
            {
            "code": 400,
            "description": "If a unknown field is submited"
            }
        ]
    }

def make_delete(name, type_name):
    return {
        "@id": "_:{}_delete".format(name),
        "@type": "http://schema.org/DeleteAction",
        "method": "DELETE",
        "label": "Deletes a Event entity",
        "description": null,
        "expects": null,
        "returns": type_name,
        "statusCodes": [
            {
            "code": 404,
            "description": "If the entity wasn't found."
            },
            {
            "code": 200,
            "description": "If the entity was deleted successfully."
            }
        ]
    }


def make_collection_post(operation_prefix, type_id, expects_type, returns_type):
        return {
          "@id": "_:{}_create".format(operation_prefix),
          "@type": "http://schema.org/AddAction",
          "method": "POST",
          "label": "Creates a new entity",
          "description": None,
          "expects": expects_type,
          "returns": returns_type,
          "statusCodes": [
            {
              "code": 201,
              "description": "If the entity was created successfully."
            }
          ]
        }

def make_collection_get(operation_prefix, type_id, expects_type, returns_type):
        return {
          "@id": "_:{}_collection_retrieve".format(operation_prefix),
          "@type": "hydra:Operation",
          "method": "GET",
          "label": "Retrieves all entities",
          "description": None,
          "expects": None,
          "returns": type_id,
          "statusCodes": [
            {
              "code": 200,
              "description": "If all entries are available"
            }]
        }

def get_operations(name, type_name):
    operations = [
        make_get,
        make_put,
        make_patch,
        make_delete
    ]

    return [op(name, type_name) for op in operations]


def get_collection_operations(operation_prefix, type_id, expects_type, returns_type):
    operations = [
        make_collection_post,
        make_collection_get
    ]

    return [op(operation_prefix, type_id, expects_type, returns_type) for op in operations]



def generate_collection_doc(
    hydra_title = "events"
    , label = "EventCollection"
    , description = "A collection of events"
    , description_retrieve = "Retrieves all entities"
    , operation_prefix = "event"):
    return {
          "hydra:title": hydra_title,
          "hydra:description": description,
          "required": None,
          "readonly": True,
          "writeonly": False,
          "property": {
            "@id": "vocab:EntryPoint/" + hydra_title,
            "@type": "hydra:Link",
            "label": hydra_title,
            "description": description,
            "domain": "vocab:EntryPoint",
            "range": "vocab:" + label,
            "supportedOperation": [
              {
                "@id": "_:{}_collection_retrieve".format(operation_prefix),
                "@type": "hydra:Operation",
                "method": "GET",
                "label": description_retrieve,
                "description": None,
                "expects": None,
                "returns": "vocab:" + label,
                "statusCodes": []
              }
            ]
          }
        }