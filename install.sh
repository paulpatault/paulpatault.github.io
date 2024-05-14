#!/bin/sh
# Copyright (c) 2024 Paul Patault (www.paulpatault.fr)
# Distributed under the MIT License

python3 -m venv env
. env/bin/activate
python -m pip install python-lsp-server jinja2
