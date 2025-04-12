@echo off
setlocal enabledelayedexpansion

echo. > config_new.json
:: Check if python is installed
where python.exe >nul 2>nul
if not errorlevel 1 (
    echo Found Python on system!
    set PYTHON_CMD=python
)

:: If python isn't the command, check for python3
if not defined PYTHON_CMD (
    where python3.exe >nul 2>nul
    if not errorlevel 1 (
        echo Found Python on system!
        set PYTHON_CMD=python3
    )
)

:: If python isn't found
if not defined PYTHON_CMD (
    echo Python was not found on this system
    echo Please install Python, then try again.
    pause
    exit
)

:: Loop through each line in the JSON file
for /f "delims=" %%A in (config.json) do (
    set "line=%%A"
    if "!line!"=="" (
        goto :continue
    )
    :: Check if the line is the "python_exe" key and update the value
    echo !line! | find "python_exe" >nul && set "found=true" || set "found=false"
    
    if !found!==true (
        echo     "python_exe" : "!PYTHON_CMD!", >> config_new.json
    ) else (
        echo !line! >> config_new.json
    )
)


endlocal
more config_new.json +1 > config.json 
del config_new.json

:: install requirements if needed
%PYTHON_CMD% utils\check_requirements.py -p %PYTHON_CMD%

:: run app
flask run --debug --host=0.0.0.0
::@echo on
::%PYTHON_CMD% --version
pause