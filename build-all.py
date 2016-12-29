#!/usr/bin/env python

"""
Script to run conda-build-all with the command line flags we usually want:

Done in python so it will work on all platforms

NOTE: the upload will only work if you have a BINSTAR_TOKEN environment variable set.

"""
import os
import subprocess

# make sure tools are up to date:
subprocess.check_call(["conda", "update", "-y", "setuptools", "pip"],
                      shell=False)

# NOTE: conda-build-all had a bug with conda-build versions 2.0.11 and 2.0.12
#       hopefully this is fixed at some point
subprocess.check_call(["conda", "install", "-y", "conda-build==2.0.10"],
                      shell=False)

subprocess.check_call(["conda", "update", "-y", "anaconda-client"],
                      shell=False)

subprocess.check_call(["conda", "update", "-y", "conda-build-all", "--channel", "conda-forge"],
                      shell=False)

# adding a channel multiple times seems to put it on the list in front of defaults,
#   which we may not want
# subprocess.check_call(["conda", "config", "--add", "channels", "NOAA-ORR-ERD"],
#                      shell=False)

this_env = os.environ.copy()
# add a dummy environment variable, so that you can use "numpy x.x"
# see: https://github.com/SciTools/conda-build-all/issues/45
# the actual value isn't used, but it needs to be a valid value (i.e. '00' does not work)
this_env["CONDA_NPY"] = "111"

# This is the command:
# conda-build-all ./ --matrix-conditions "python 2.7.*" --inspect-channels NOAA-ORR-ERD --upload-channels NOAA-ORR-ERD

subprocess.check_call(["conda-build-all", "./",
                       "--matrix-conditions", "python 2.7.*","numpy >=1.11",
                       "--inspect-channels", "NOAA-ORR-ERD",
                       "--upload-channels", "NOAA-ORR-ERD",
                       "--no-inspect-conda-bld-directory",  #  ensures that it re-builds and uploads stuff that was already build by hand
                       "--artefact-directory", "packages"
                       ],
                      shell=False,
                      env=this_env)
