#!/bin/bash
set +e
cd ./oil_library/
# $PYTHON ./setup.py remake_oil_db do this post install somehow.
$PYTHON -m pip install ./