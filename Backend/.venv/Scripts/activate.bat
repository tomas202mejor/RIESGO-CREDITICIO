@echo off

rem This file is UTF-8 encoded, so we need to update the current code page while executing it
for /f "tokens=2 delims=:." %%a in ('"%SystemRoot%\System32\chcp.com"') do (
    set _OLD_CODEPAGE=%%a
)
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" 65001 > nul
)

<<<<<<< HEAD:Backend/venv/Scripts/activate.bat
set "VIRTUAL_ENV=C:\Users\janni\RIESGO-CREDITICIO\Backend\venv"
=======
set VIRTUAL_ENV=C:\Users\Usuario\OneDrive - uniminuto.edu\Escritorio\RIESGO-CREDITICIO\Backend\.venv
>>>>>>> 9667c03d8008c7ceb3a45ed06e419c8191661515:Backend/.venv/Scripts/activate.bat

if not defined PROMPT set PROMPT=$P$G

if defined _OLD_VIRTUAL_PROMPT set PROMPT=%_OLD_VIRTUAL_PROMPT%
if defined _OLD_VIRTUAL_PYTHONHOME set PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%

<<<<<<< HEAD:Backend/venv/Scripts/activate.bat
set "_OLD_VIRTUAL_PROMPT=%PROMPT%"
set "PROMPT=(venv) %PROMPT%"
=======
set _OLD_VIRTUAL_PROMPT=%PROMPT%
set PROMPT=(.venv) %PROMPT%
>>>>>>> 9667c03d8008c7ceb3a45ed06e419c8191661515:Backend/.venv/Scripts/activate.bat

if defined PYTHONHOME set _OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%
set PYTHONHOME=

if defined _OLD_VIRTUAL_PATH set PATH=%_OLD_VIRTUAL_PATH%
if not defined _OLD_VIRTUAL_PATH set _OLD_VIRTUAL_PATH=%PATH%

<<<<<<< HEAD:Backend/venv/Scripts/activate.bat
set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"
set "VIRTUAL_ENV_PROMPT=venv"
=======
set PATH=%VIRTUAL_ENV%\Scripts;%PATH%
set VIRTUAL_ENV_PROMPT=(.venv) 
>>>>>>> 9667c03d8008c7ceb3a45ed06e419c8191661515:Backend/.venv/Scripts/activate.bat

:END
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" %_OLD_CODEPAGE% > nul
    set _OLD_CODEPAGE=
)
