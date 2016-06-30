#!/bin/bash

# $PYTHON setup.py install --single-version-externally-managed  --record record.txt
# regex doesn't use setuptools, so use the pip method:
pip install --no-cache-dir --no-deps --compile ./