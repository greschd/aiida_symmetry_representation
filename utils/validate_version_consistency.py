#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple script that checks the consistency between the version number specified in
setup.json, and the version in the __init__.py file.
"""

import os
import re
import sys
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(SCRIPT_DIR, os.path.pardir)

# Get the __init__.py version number
with open(
    os.path.join(ROOT_DIR, 'aiida_symmetry_representation/__init__.py')
) as f:
    MATCH_EXPR = "__version__[^'\"]+(['\"])([^'\"]+)"
    VERSION_INIT = re.search(MATCH_EXPR, f.read()).group(2).strip()

# Get the setup.json version number
with open(os.path.join(ROOT_DIR, 'setup.json')) as f:
    VERSION_JSON = json.load(f)["version"]

if VERSION_INIT != VERSION_JSON:
    print(
        "Version numbers don't match: init:'{}', json:'{}' ".format(
            VERSION_INIT, VERSION_JSON
        )
    )
    sys.exit(1)
