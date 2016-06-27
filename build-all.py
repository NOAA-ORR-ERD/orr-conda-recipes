#!/usr/bin/env python

"""
Script to run conda-build-all with the command line flags we usually want:

Done in python so it will work on all platforms
"""

import subprocess

# make sure tools are up to date:
subprocess.check_call(["conda", "update", "conda-build"],
                      shell=False)

subprocess.check_call(["conda", "update", "anaconda-client"],
                      shell=False)

subprocess.check_call(["conda", "update", "conda-build-all", "--channel", "conda-forge"],
                      shell=False)

subprocess.check_call(["conda", "config", "--add", "channels", "NOAA-ORR-ERD"],
                      shell=False)

# This is the command:
# conda-build-all ./ --matrix-conditions python 2.7.* --inspect-channels NOAA-ORR-ERD --upload-channels NOAA-ORR-ERD

subprocess.check_call(["conda-build-all", "./",
                       "--matrix-conditions", "python 2.7.*",
                       "--inspect-channels", "NOAA-ORR-ERD",
                       "--upload-channels", "NOAA-ORR-ERD",
                       ], shell=False)
