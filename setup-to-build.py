#!/usr/bin/env python

"""
Script to get all the pacakges needed for bulding setup and installed in the right versions
"""
import os
import subprocess

# doing this to make sure the channels are all in the right order

subprocess.check_call(["conda", "config", "--add", "channels", "defaults"],
                      shell=False)

subprocess.check_call(["conda", "config", "--add", "channels", "NOAA-ORR-ERD"],
                      shell=False)

subprocess.check_call(["conda", "config", "--add", "channels", "conda-forge"],
                      shell=False)


# make sure tools are up to date:
subprocess.check_call(["conda", "install", "-y", "setuptools", "pip"],
                      shell=False)

# NOTE: conda-build-all had a bug with conda-build versions 2.0.11 and 2.0.12
#       hopefully this is fixed at some point
subprocess.check_call(["conda", "install", "-y", "conda-build"],
                      shell=False)

subprocess.check_call(["conda", "install", "-y", "anaconda-client"],
                      shell=False)

subprocess.check_call(["conda", "install", "-y", "conda-build-all", "--channel", "conda-forge"],
                      shell=False)


