import ctx

VOCAB_URL = "{}/api/vocab".format(ctx.base_url)
LINK_HEADER = { 
    "link": '<{}>; rel="http://www.w3.org/ns/hydra/core#apiDocumentation"'.format(VOCAB_URL)
}