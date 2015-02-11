@echo off

REM --- This file runs the setup.py script.
REM --
REM -- This script is meant to be launched by Inno Setup (but can also be
REM -- started manually).
REM --
REM -- Please put OS-independant actions into setup.py.

echo = Cleaning up output =
REM -- Remove residual generated runtime files
rmdir /S /Q output-py2exe
rmdir /S /Q output-setup

REM -- Run Py2exe
python setup.py py2exe
if not %errorlevel%==0 goto error

REM -- Remove intermediate build files
echo.
echo = Deleting temporary build files =
rmdir /S /Q build

REM -- Done
echo.
echo All done OK
goto end

REM -- Error
:error
echo.
echo ### AN ERROR OCCURED ###
pause
exit /B -1

:end
