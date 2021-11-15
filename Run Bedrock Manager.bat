@echo off


taskkill /F /IM "bedrock_server.exe" /T

"C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\python.exe" -m pip install requests
"C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\python.exe" -m pip install beautifulsoup4
"C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\python.exe" -m pip install wget

set scriptbase=%~dp0

cd %scriptbase%

Bedrock_Manager.py
