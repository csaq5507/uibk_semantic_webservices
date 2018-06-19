
import os

template_root = os.path.join(os.path.dirname(__file__), "resources", "templates")

def render(variables, template_name):
    content = ""
    with open(os.path.join(template_root, template_name)) as file:
        content = file.read()

    for name in variables:
        value = variables[name]
        content = content.replace("%{}%".format(name), value)
    return content

