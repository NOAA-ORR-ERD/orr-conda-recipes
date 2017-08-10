:: LOTS more to do here!

:: This should build the package -- but not tested, and I'm sure there more to it.
:: cd wxPython
:: call "%HOMEPATH%\AppData\Local\Programs\Common\\Microsoft\Visual C++ for Python\9.0\vcvarsall.bat" amd64
:: "%PYTHON%" build-wxpython.py --prefix=$PREFIX --build_dir=../bld  --install

:: This version smiply installs the wheels from Chris Gohlke's repo
pip install wxPython_common-3.0.2.0-py2-none-any.whl
pip install wxPython-3.0.2.0-cp27-none-win_amd64.whl

