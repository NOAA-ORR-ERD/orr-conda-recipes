#################
orr-conda-recipes
#################

Recipes for building conda packages for many (all?) of the third party packages required by ORR tools -- specifically GNOME

This repo should give you all you need to build conda packages for various third party tools needed by py_gnome. In theory, these will be built by ERD developers, and provided on anaconda.org in the NOAA-ORR-ERD channel. But if you want to build them yourself (or you are an ERD developer), this is how to do it.

Getting set up
###############

requirements
----------------

To build packages, you'll need the basic stuff for building and working with anaconda.org::

  conda install conda-build
  conda install anaconda-client

Then you'll want to add the NOAA-ORR-ERD channel::

  conda config --add channels NOAA-ORR-ERD

Ideally, you won't have any other anaconda channels set up -- or conda may find packages in channels other than the NOAA-ORR-ERD one. You can remove a channel with::

  conda config --remove channels ChrisBarker-NOAA -f

[You can also simply edit the ``~/.condarc`` file, which will clean out all config, and then start again]

Note that conda build can only be run in the main root environment, so you may want to setup a new miniconda install to get a really clean system.

http://conda.pydata.org/miniconda.html

Setting up anaconda.org
-----------------------

It can be helpful to login to your anaconda account before building / uploading packages::

  anaconda login

This, of course, assumes you have an anaconda.org account. If you want to distribute packages using anaconda.org, go set one up if you don't

https://anaconda.org


conda build-all
---------------

To build all the packages, you can use Phil Elson's lovely conda-build-all tool:

  conda build-all is a conda subcommand which allows multiple distributions to be built (and uploaded) in a single command. 

https://github.com/SciTools/conda-build-all

Installing conda-build-all
..........................

First you will need to install `conda-build-all` itself.

You can get it from the conda-forge channel:

  conda install conda-build-all --channel conda-forge

If not, you can build it yourself from the source in the gitHub repo.

Using `conda build-all`, you can build all binaries in this repository, ordered by their dependencies.  `conda build-all` can check which packages are already on the channel and does not build any that are already there. It can also build for a whole matrix of python and numpy versions -- we'll set up the scripts to do only what we need for ORR/ERD work.

Using conda-build-all
.....................

Getting `conda-build-all`` working on your system:

Make sure you have the NOAA-ORR-ERD channel set up::

  conda config --add channels NOAA-ORR-ERD -f

Clone the orr-conda-recipes repo, if you haven't already::

  git clone https://github.com/NOAA-ORR-ERD/orr-conda-recipes.git

Use `conda-build-all` to build everything::

  python build-all.py

(run from inside the orr-conda-recipes dir)

This runs the following conda-build-all command::

    conda-build-all ./ --matrix-conditions "python 2.7.*" \
                       --inspect-channels NOAA-ORR-ERD \
                       --upload-channels NOAA-ORR-ERD

Note that `--matrix-conditions "python 2.7.*"` means only python2.7 -- otherwise, it will try to build for a whole  matrix of python versions -- 2.6 to 3.5. Which is pretty cool, but we're only trying to support 2.7 now. It can also build for multiple numpy versions, but this way it builds for the one installed in your conda setup.

If you are a NOAA-ORR-ERD anaconda.org admin, or you are building for your own personal repository, you may want to upload the packages as you build. The above script will do that for you if you set a `BINSTAR_TOKEN`::

    TOKEN=$(anaconda auth -n NAME-OF-YOUR-TOKEN --max-age 22896000 -c --scopes api)
    export BINSTAR_TOKEN=$TOKEN

## note: this may now be called a ANACONDA_TOKEN, but this worked last I tried

If you are going to do this more than once, you may want to set that token in your shell init script -- i.e. ~/.bash_profile::

  BINSTAR_TOKEN=Ch-3grt7fher23-de39-4382-9er0-c3138fj3686

And no, that is not a real token ;-) -- you need to put the one you generate in there. You can use::

    echo $TOKEN

to get it.

Building / Uploading one by one
-------------------------------

If you have just one package to add or update, it may be easier to simply build and upload that one package by hand::

  $ conda build the_package
  $ anaconda upload --user noaa-orr-erd THE_FULL_PATH_TO_THE_TARBALL_CONDA_BUILD_REPORTS
  







