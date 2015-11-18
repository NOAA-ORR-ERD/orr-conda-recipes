#################
orr-conda-recipes
#################

Recipes for building conda packages for many (all?) of the third party packages required by ORR tools -- specifically GNOME

This repo should give you all you need to build conda packages for various third party tools needed by py_gnome. In theory, these will be built by ORR developers, and provided on binstar in the NOAA-ORR-ERD channel. But if you want to build them yourself, this is how to do it.

Getting set up
###############

requirements
----------------

To build packges, you'll need the basic stuff for building and working with anaconda.org::

  conda install conda-build
  conda install anaconda-client

Then you'll want to add the NOAA-ORR-ERD channel::

  conda config --add channels NOAA-ORR-ERD

Ideally, you won't have any other anaconda channels set up -- or conda my find packages in other channels than the NOAA-ORR-ERD one. You can remove a channel with::

  conda config --remove channels ChrisBarker-NOAA -f

[You can also simply edit the ``~/.condarc`` file, which will clean out all config, and then start again]

Note that conda build can only be run in the main root environment, so you may want to setup a new miniconda install to get a really clean system.

Setting up anaconda.org
-----------------------

It can be helpful to login to your anaconda account before bulding / uploading packages::

  anaconda login


Obvious-CI
----------

To build all the packages, you can use Phil Elson's lovely obvious-ci scripts:

  Obvious-CI is a collection of tools that help with continuous integration like travis-ci (https://travis-ci.org/ioos/conda-recipes/builds) and AppVeyor (https://ci.appveyor.com/project/comtbot/conda-recipes/history).

But is also helpful for simply  building on your local machine.

https://github.com/pelson/Obvious-CI

Installing Obvious-CI
.....................

First you will need to install obvious-ci itself.

It should be in the onoaa-orr-erd channel already::

  conda install obvious-ci

If not, you can build it yourself from the recipe in orr-conda-packages

  conda build obvious-ci

And then you may need to upload it to the NOAA-ORR-ERD channel::

  anaconda upload --user noaa-orr-erd THE_FULL_PATH_TO_THE_TARBALL_CONDA_BUILD_REPORTS

Or you could build and install from the gitHub repo.

Using Obvious-CI, the single script `obvci_conda_build_dir.py` can build all binaries in this repository, ordered by their dependency.  Note that `obvci_conda_build_dir.py` reads the packages that are already on the channels and does not build if they are the same. Note that with recent version, it will try to build a full matrix of versions (py2 and 3, different numpy versions..), so you probably want to pass in arguments to restrict that -- see below.

Using Obvious-CI
.................

Here's how to get the script working on your system:

Make sure you have the NOAA-ORR-ERD channel set up::

  conda config --add channels NOAA-ORR-ERD -f

Clone the orr-conda-recipes repo, if you haven't already::

  git clone https://github.com/NOAA-ORR-ERD/orr-conda-recipes.git

Use obvious-ci to build everything::

  obvci_conda_build_dir ./ NOAA-ORR-ERD --channel main --build-condition "python >=2.7,<3"

(run from the orr-conda-recipes dir)

The last command will build everything in the git repo against the `NOAA-ORR-ERD` channel.

Note that the "python >=2.7,<3" part means only python2.7 -- otehrwise, it will try to build for a whole  matrix of python versions -- 2.6 to 3.5. Which is pretty cool, but we're only trying to support 2.7 now.

If you are a NOAA-ORR-ERD anaconda.org admin, or you are building for your own personal repository, you may want to upload the packages as you build. The `obvci_conda_build_dir` script will do that for you if you set a `BINSTAR_TOKEN`::

    TOKEN=$(anaconda auth -n NAME-OF-YOUR-TOKEN --max-age 22896000 -c --scopes api)
    export BINSTAR_TOKEN=$TOKEN

## note: this may now be called a ANACONDA_TOKEN, but this worked last I tried

If you are going to do this more than once, you may want to set that token in your shell init script -- i.e. ~/.bash_profile::

  BINSTAR_TOKEN=Ch-3grt7fher23-de39-4382-9er0-c3138fj3686

And no, that is not a real token ;-) -- you need to put the one you generate in there. You can use::

    echo $TOKEN

to get it.

Building / Uploading one by one
................................

If you have just one package to add, it may be easier to simply build and upload that one package by hand::

  $ conda build the_package
  $ anaconda upload --user noaa-orr-erd THE_FULL_PATH_TO_THE_TARBALL_CONDA_BUILD_REPORTS
  







