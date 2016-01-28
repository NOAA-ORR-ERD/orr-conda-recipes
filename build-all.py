#!/usr/bin/env python

"""
Script to run conda-build-all with the command line flags we usually want:

Done in python so it will work on all platforms
"""

import subprocess

subprocess.check_call(["conda-build-all", "./",
                        "--matrix-conditions","python 2.7.*",
                        "--inspect-channels","NOAA-ORR-ERD",
                        "--upload-channels","NOAA-ORR-ERD",
                        ], shell=False)
