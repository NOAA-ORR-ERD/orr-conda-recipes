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

Important Note About Building On Linux
--------------------------------------

The conda-build process sets up a PREFIX path for building an anaconda virtual
environment.  This environment is used for building and testing the built
package in isolation, which is a reasonable thing to do.  But this PREFIX path
is made to contain placeholder text to make it really long.

The reason that they make it really long is because shared libraries may need
to be re-linked upon installation, and they contain statically built
binary headers in which it is likely not possible to allocate extra storage
for a longer path after the library is initially built.  Basically, you can
re-link the library with shorter paths, but probably not a longer one.

Ok, so why is this a problem on linux?  Well, the current PREFIX path length
set by conda-build is 255.  And this is fine as far as I know for building
Linux libraries.  But if your setup.py contains any post processing scripts,
such as the OilLibrary database initialization script, then setuptools will
build that script with a hash-bang, or 'shebang' ('#!') header on the first
line of the script that contains a path to the python executable using the
PREFIX path.  For the sake of readability, here is an example of a normal
shebang script:

    #!/usr/bin/env python
    import sys
    print sys.prefix

The maximum length of the interpreter path in the first line is limited
in the kernel by BINPRM_BUF_SIZE, set in include/linux/binfmts.h.
And a typical linux distribution sets it to 127 characters.  So when
conda-build generates a script using a PREFIX to 256, it creates a script that
exceeds the maximum interpreter path length, and the script cannot be run.

And the error you get is very misleading:

    $ ls -l ./initialize_OilLibrary_db
    -rwxrwxr-x 1 jamesm jamesm 678 Sep  3 13:17 ./initialize_OilLibrary_db
    $ ./initialize_OilLibrary_db
    -ksh: ./initialize_OilLibrary_db: not found [No such file or directory]

Yeah...the file exists and is executable, but when we try to execute it,
the file doesn't exist.  In actuality, it is the interpreter specified by the
shebang that doesn't exist, because it has been truncated.

Please note that this problem does not seem to happen on MacOSX or Windows,
just Linux.

So what should we do about this?

**Option 1:**

We could change the limit in binfmts.h and recompile our linux kernel.  That
would certainly work, but is kind of heavy handed.  I am sure most of us would
not want to do that.

**Option 2:**

Fortunately, conda-build comes with a command-line argument that will set the
size of PREFIX F(--prefix-length LEN).  So if we set our PREFIX to a value
that is less than 127 - len('/bin/python\n'), which works out to **114**,
this will work.

    $ conda build oil_library --prefix_length 114
    ...
    ...
    TEST END: <build_location>/oil_library-1.0.5-py27_1.tar.bz2  # for example
    ...
    $
