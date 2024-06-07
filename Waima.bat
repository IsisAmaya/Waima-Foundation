@echo off
start "" python manage.py runserver
timeout /t 2 /nobreak >nul
start "" http://localhost:8000
