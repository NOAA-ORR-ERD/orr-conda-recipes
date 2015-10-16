#!/bin/sh

# build script for libgd -- tested on OS-X

## this should let configure find the png, etc libs
export CFLAGS="-I$PREFIX/include $CFLAGS"
export LDFLAGS="-L$PREFIX/lib $LDFLAGS"

## note: not using fontconfig and xpm, because those are not out of the box with anaconda
##       and we dont want configure to find versions that may be
##       installed with homebrew, etc.

./configure --prefix=$PREFIX \
            --with-png=$PREFIX \
            --with-freetype=$PREFIX \
            --with-tiff=$PREFIX \
            --with-fontconfig=no \
            --with-xpm=no \

make

make install




