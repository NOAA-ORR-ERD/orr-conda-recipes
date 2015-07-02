#################
orr-conda-recipes
#################

Recipes for building conda packages for many (all?) of the third party packages required by ORR tools -- specifically GNOME

This repo should give you all you need to build conda pacakges for various third party tools needed by py_gnome. IN theoery, these will be built by ORR developers, and provided on binstar in the NOAA-ORR-ERD channel. But you you want to build yourself, this is how to do it.

Getting set up
###############

requirements
----------------

To build packges, you'll need the basic stuff for building and working with binstar::

  conda install conda-build
  conda install binstar

Then you'll want to add the NOAA-ORR-ERD channel::

  conda config --add channels NOAA-ORR-ERD

Ideally, you won't have any other binstar channels set up -- or conda my find packages in other channels than the NOAA-ORR-ERD one. You can remove a channel with::

  conda config --remove channels ChrisBarker-NOAA -f

[You can also smply the the ``~/.condarc`` file, which will clean out all config, and then start again]

Note that conda build can only be run in the main root environment, so you may want to setup a new miniconda environment to get a really clean system.

Setting up binstar
-------------------

You may want to have conda automatically upload newly built packages:

   conda config --set binstar_upload yes

It can be helpful to login to your binstar account before bulding / uploading packages::

  binstar login



Obvious-CI
----------

To build all the packages, you can use Phil Elson's lovely obvious-ci scripts:

Obvious-CIis a collection of tools that help with continuous integration like travis-ci (https://travis-ci.org/ioos/conda-recipes/builds) and AppVeyor (https://ci.appveyor.com/project/comtbot/conda-recipes/history). But is also helpful for simply  building on your local machine.

https://github.com/pelson/Obvious-CI

First you will need to install obvious-ci itself::

  conda install obvious-ci

or, if you are doing this totally from scratch, you can built it yourself::

  conda build obvious-ci

And then you may need to upload it to the NOAA-ORR-ERD channel::

  binstar upload --user noaa-orr-erd THE_FULL_PATH_TO_THE_TARBALL_CONDA_BUILD_REPORTS

Using Obvious-CI, the single script `obvci_conda_build_dir.py` can build all binaries in this repository, ordered by their dependency.  Note that `obvci_conda_build_dir.py` reads the packages that are already on the channels and does not build if they are the same.

Here's how to get the script working on your system:: 

  conda config --add channels NOAA-ORR-ERD -f

  conda install obvious-ci

  git clone https://github.com/NOAA-ORR-ERD/orr-conda-recipes.git

  obvci_conda_build_dir.py ./orr-conda-recipes NOAA-ORR-ERD --channel main


The last command will build everything in the git repo against the `NOAA-ORR-ERD` channel.

If you are a NOAA-ORR-ERD binstar admin, or you are building for your own personal repository, you may want to upload the packages as you build.  The `obvci_conda_build_dir.py` script will do that for you if you set a `BINSTAR_TOKEN`::

    TOKEN=$(binstar auth -n NAME-OF-YOUR-TOKEN --max-age 22896000 -c --scopes api)
    export BINSTAR_TOKEN=$TOKEN

