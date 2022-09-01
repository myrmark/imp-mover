#!/bin/python3

#Author Filip Malmberg

"""
This script checks if there are any files in the imp folder, and asks the user if they want to delete the files.
They can then copy a new IMP image from the imp_images folder to the imp folder

Prerequisite: 
- pick (installed with "pip3 install pick")
- a imp_images folder located in /opt/icomera/ivalde/img containing IMP-images to copy from
- cm permission to remove/move files in /opt/icomera/ivalde/img/imp and imp_images
"""

import os
import subprocess

from pick import pick

try:
    os.listdir("/opt/icomera/ivalde/img/imp_images")
except Exception:
    print("---WARNING---\n"
        "\n"
        "The imp_images folder was not found!\n"
        "\n"
        "---WARNING---\n")
    exit()

current_Imp = os.listdir("/opt/icomera/ivalde/img/imp")

if len(current_Imp) != 1:
    print("---WARNING---\n"
        "\n"
        "One or more files were found in the active IMP folder.\n"
        "You need to clear all files from the folder before you continue\n"
        "\n"
        "---WARNING---\n")
    while True:
        answer = input("Do you want to clear all files from the active IMP folder? [y/N]: ")
        if answer.lower() in ["y","yes"]:
            for f in current_Imp:
                os.remove("/opt/icomera/ivalde/img/imp/{}".format(f))
                break
        elif answer.lower() in ["n","no"]:
            break
        else:
            print("Please answer yes or no")
elif len(current_Imp) == 1:
    print("The following file was found in the imp folder: {}".format(current_Imp[0]))
    while True:
        answer = input("Do you want to delete the file and continue? [y/N]: ")
        if answer.lower() in ["y","yes"]:
            os.remove("/opt/icomera/ivalde/img/imp/{}".format(current_Imp[0]))
            break
        elif answer.lower() in ["n","no"]:
            exit()
        else:
            print("Please answer yes or no")

print("\n"
    "Please note that Eitre will use the first IMP image it can see in the folder\n")

while True:
    answer = input("Do you want to continue anyway? [y/N]:")
    if answer.lower() in ["y","yes"]:
        break
    elif answer.lower() in ["n","no"]:
        exit()
    else:
        print("Please answer yes or no")

available_Imps = os.listdir("/opt/icomera/ivalde/img/imp_images")
if len(available_Imps) == 0:
    print("\n"
        "No available IMP images found\n"
        "Aborting script")
    exit()

title = 'Select the IMP you want to use: '
option, index = pick(available_Imps, title)

subprocess.call('cp /opt/icomera/ivalde/img/imp_images/{} /opt/icomera/ivalde/img/imp/'.format(option), shell=True) 

if option in os.listdir("/opt/icomera/ivalde/img/imp/"):
    print("Successfully copied IMP image")
else:
    print("Script was unsuccessful in copying the IMP image")
