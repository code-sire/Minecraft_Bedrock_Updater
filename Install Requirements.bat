@echo off

set scriptbase=%~dp0

cd %scriptbase%

"C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\python.exe" -m pip install -r %scriptbase%\requirements.txt
