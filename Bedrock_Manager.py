
#################################################################
# Importing Native Modules
#################################################################
import os
import shutil
from zipfile import ZipFile
import subprocess


#################################################################
# Importing Downloaded Modules
################################################################
import requests
import wget
from bs4 import BeautifulSoup



#################################################################
# Global Variables
#################################################################

# This is the URL of the site to check
lookup_link = "https://www.minecraft.net/en-us/download/server/bedrock"

# User Profile Location
HomeDir = os.path.expanduser("~")

# Minecraft Install Location
mc_install_loc = HomeDir + '/Documents/MC_Install'

# Staging Folder
mc_staging = mc_install_loc + '/Extract_Staging'

# This is where downloaded files will be tracked.
tracking_file = "file_tracking.txt"

# Current_File
curr_file = ''

# This is just a trigger to see if we can move to the next step.
extract_needed = 0

#################################################################
# Functions
#################################################################

def SetDetailsAndFile():
    global extract_needed
    global curr_file

    # Set User Agent
    headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30"}

    # Request and fetch the webpage contents
    response = requests.get(lookup_link, headers=headers)
    webpage = response.content

    # Create a Beautiful Soup Object
    soup = BeautifulSoup(webpage, "html.parser")

    # Gets all the links on the page
    for a_href in soup.find_all("a", href=True):

        # Singles out the Windows Download link
        if "bin-win" in a_href["href"]:
            to_download = a_href["href"]

            # Gets the file name out of the URL
            available_file = os.path.basename(to_download)

            # Opens the Tracking File
            read_file = open(tracking_file, "r")

            # Checks to see if the filename is in the tracking file.
            if available_file in read_file.read():
                # We have the file and there is not thing to do.
                print("Running Current Version")
                read_file.close()
                extract_needed = 0

            else:
                read_file.close()
                print("Downloading Latest Version")
                wget.download(to_download)
                write_file = open(tracking_file, "a")
                write_file.write(available_file + " \n")
                write_file.close()
                curr_file = available_file
                extract_needed = 1


def MoveZipFile():

    # Make sure that our extract path exists
    if not os.path.exists(mc_staging):  # os.path.join() for making a full path safely
        os.makedirs(mc_staging)  # If not create the directory, inside their home directory
    else:
        pass

    shutil.move(curr_file, mc_staging + "/" + curr_file)


def ExtractZip():

    # open the zip file in read mode
    with ZipFile(mc_staging + "/" + curr_file, 'r') as zip:

        # extract all files
        print('Extracting the New Version')
        zip.extractall(mc_staging)
        print('Done Extracting')


def UpdateFiles():
    print('Merging in Updates')
    skiplist = ['permissions.json', 'server.properties', 'whitelist.json']

    # Getting filenames of the files at the source.
    for src_dir, dirs, files in os.walk(mc_staging):
        dst_dir = src_dir.replace(mc_staging, mc_install_loc, 1)

        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        else:
            pass

        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if file_ not in skiplist:
                if os.path.exists(dst_file):
                    os.remove(dst_file)
                else:
                    pass

                if file_.endswith(".zip"):
                    os.remove(src_file)
                else:
                    shutil.move(src_file, dst_dir)

            else:
                pass

    print('Updates Complete')


def StartServer():
    print('Starting Server')
    subprocess.Popen(mc_install_loc + '/bedrock_server.exe', stdout=None, stderr=None, stdin=None, close_fds=True)


#################################################################
# Activator Code
#################################################################

# Checking to see if there is a new file.
SetDetailsAndFile()

# If there is a new file we will move and extract it.
if extract_needed == 0:
    print("No Update Needed")
else:
    print("Update Needed")
    MoveZipFile()
    ExtractZip()
    UpdateFiles()

StartServer()
