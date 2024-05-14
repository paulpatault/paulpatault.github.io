# Copyright (c) 2024 Paul Patault (www.paulpatault.fr)
# Distributed under the MIT License

import os, sys
from jinja2 import Environment, PackageLoader, select_autoescape


filename = sys.argv[1]
if filename == "layout.html": exit(0)

f = os.path.join("html/templates", filename)
assert os.path.isfile(f)

env = Environment(
    loader=PackageLoader("html"),
    autoescape=select_autoescape()
)

template = env.get_template(filename)

with open(filename, "w") as f:
    f.write(template.render())
