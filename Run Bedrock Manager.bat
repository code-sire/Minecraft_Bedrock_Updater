@echo off

taskkill /F /IM "bedrock_server.exe" /T

set scriptbase=%~dp0

cd %scriptbase%

Bedrock_Manager.py
