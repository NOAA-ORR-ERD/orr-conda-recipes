rem $PYTHON setup.py install --single-version-externally-managed  --record record.txt
rem pyproj doesn't use setuptools, so use the pip method:
pip install --no-cache-dir --no-deps --compile ./

if errorlevel 1 exit 1
