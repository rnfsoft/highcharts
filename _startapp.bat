@echo off

set /p app="Enter a new App name: "
cmd /k "cd Scripts & activate & cd .. & cd src & python manage.py startapp %app% & cd %app% & mkdir templates & cd templates & mkdir %app%