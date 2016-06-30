rem $PYTHON setup.py install --single-version-externally-managed  --record record.txt
rem regex doesn't use setuptools, so use the pip method:
pip install --no-cache-dir --no-deps --compile ./

if errorlevel 1 exit 1

:: Add more build steps here, if they are necessary.

:: See
:: http://docs.continuum.io/conda/build.html
:: for a list of environment variables that are set during the build process.
