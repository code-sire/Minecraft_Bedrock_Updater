# Minecraft Bedrock Updater

Note: First and foremost, this tool was designed with Windows in mind. I know a few modifications will need to be made in order to run this on Linux.

## What does it do?
This tool was created to help keep your Bedrock server current.

1. It stops the Bedrock-Server.exe gracefully.
2. The tool scrapes the Mincraft.net Bedrock download page for the link to the current version of the server.
3. It downloads the current version
4. It assess to see if you need the version that you just downloaded. (If you have a server running it will automatically download and overlay the current version so that it can track your future state.)
5. It updates all file except "permissions.json", "server.properties", "whitelist.json". These files are preserved.
6. It cleans up after itself
7. It starts the server backup.

## How to use it?
1. Download the Repo Zip file.
2. Extract the Zip to a place of your choosing.
3. Update "Bedrock_Manager.py" file with your Minecraft Install Location. The script uses "HomeDir" to locate the User's Profile folder. You can use that as a base or put the whole path. If you do use a full path you will need to put an "r" before your quoted path. Example: mc_install_loc = r'C:\Minecraft'
4. Save your changes
5. Execute "Run Bedrock Manager.bat" (I would suggest using Windows Task Scheduler and having this run at 1:00 AM local time.)
