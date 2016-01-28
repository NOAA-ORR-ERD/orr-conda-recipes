
rem These need to be set so that distutls won't try to run vcvasall.bat
rem -- shouldn't be required with the pip install (and anything compiled here anyway?)
rem set MSSDK=1 
rem set DISTUTILS_USE_SDK=1

"%PYTHON%" -m pip install --verbose ./

if errorlevel 1 exit 1

:: Add more build steps here, if they are necessary.

:: See
:: http://docs.continuum.io/conda/build.html
:: for a list of environment variables that are set during the build process.
