@echo off
set p=8000 
for /F "tokens=2 delims=:" %%i in ('ipconfig ^| findstr /IC:"IPv4 Address"') do set h=%%i:%p% 
start /B C:\"Program Files (x86)"\Google\Chrome\Application\chrome.exe "%h%" 
cmd /k "cd Scripts & activate & cd .. & cd src & python manage.py runserver %h%"



