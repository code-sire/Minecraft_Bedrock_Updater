@echo off


taskkill /F /IM "bedrock_server.exe" /T

rem "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\python.exe" -m pip install requests
rem "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\python.exe" -m pip install beautifulsoup4
rem "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\python.exe" -m pip install wget

set scriptbase=%~dp0

cd %scriptbase%

Bedrock_Manager.py
