#!/usr/bin/env python

"""
Script to run conda-build-all with the command line flags we usually want:

Done in python so it will work on all platforms

NOTE: the upload will only work if you have a BINSTAR_TOKEN environment variable set.

"""
import os
import subprocess

# make sure tools are up to date:
subprocess.check_call(["conda", "update", "conda-build"],
                      shell=False)

subprocess.check_call(["conda", "update", "anaconda-client"],
                      shell=False)

subprocess.check_call(["conda", "update", "conda-build-all", "--channel", "conda-forge"],
                      shell=False)

# adding a channel multiple times seems to put it on the list in front of defaults,
#   which we may not want
# subprocess.check_call(["conda", "config", "--add", "channels", "NOAA-ORR-ERD"],
#                      shell=False)

# add a dummy environment variable, so that you can use "numpy x.x"
# see: https://github.com/SciTools/conda-build-all/issues/45
# not working, but saved in case I figure it out
# this_env = os.environ.copy()
# this_env["CONDA_NPY"] = "00"

# This is the command:
# conda-build-all ./ --matrix-conditions "python 2.7.*" --inspect-channels NOAA-ORR-ERD --upload-channels NOAA-ORR-ERD

subprocess.check_call(["conda-build-all", "./",
                       "--matrix-conditions", "python 2.7.*",
                       "--inspect-channels", "NOAA-ORR-ERD",
                       "--upload-channels", "NOAA-ORR-ERD",
                       "--no-inspect-conda-bld-directory",
                       "--artefact-directory", "packages"
                       ],
                      shell=False,
                      env=this_env)
