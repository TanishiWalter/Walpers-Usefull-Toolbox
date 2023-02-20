#This is simple script to rename all files in forlder

from colorama import Fore as color #Renamed For to color to be more readable
import os
from pathlib import Path

systemImported = True

#This part of script is going to be in every script in this toolbox
try:
    import system #The "system" is script that contains all the useful function as printing logo, that I would have to copy manualy
except Exception as e:
    print(color.RED + "This might be error, but it also might mean that system file is not in the same folder as this script.")
    print(color.RED + "Read info.txt for more info.")
    print("If there is system file inside the same folder, error code is 04")
    print("Printing error message just to be sure:")
    print(e)
    systemImported = False

def error01(function): #This function handles errors 01 (read info.txt/RADME.md for more info)
    if systemImported == True:
            print(color.RED + "Error, the " + function + " function in system import is broken/missing.")
            print(color.RED + "Check if the system file is here? Y/N")
            checkForFile = input("> ")
            if checkForFile.lower() == "y":
                fileList = os.listdir()

                for i in fileList:
                    if i == "system.py":
                        print(color.YELLOW + "System file found, this means that the error is coming from within the system file itself.")
                        print(color.YELLOW + "Try copying the code from github.")
                        print(color.YELLOW + "If it doesn't help, contact Walper using Discord")
                        print(color.RESET)
                        break
            else:
                print("Ok, the logo printing part will be skipped.")

#This is no longer part that will be in every script

def changeFileType(path,type1,type2):
    if path == "null":
        path = os.getcwd()

    fileList = os.listdir(str(path))
    changeList = []

    for i in fileList:
        if i.split(".")[len(i.split(".")) - 1] == type1:
            changeList.append(i)
        
    for i in changeFileType:
        newType = i.split(".")[len(i.split(".")) - 1] == type2
        os.rename(i,newType)

try:
    import system #The "system" is script that contains all the useful function as printing logo, that I would have to copy manualy
except Exception as e:

    
    print(color.GREEN + "This is script to change all file extensions of one type to another.")
    print("Please, input path of folder, in which are the files to change (null to change only files in the same folder as script): ")
    path = input("> ")
    print("Please, enter the type to target: ")
    type1 = input("> ")
    print("Please, enter the type to change into: ")
    type2 = input("> ")

    changeFileType(path,type1,type2)