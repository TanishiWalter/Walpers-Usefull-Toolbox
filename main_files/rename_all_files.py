#This is simple script to rename all files in forlder

from colorama import Fore as color #Renamed For to color to be more readable
import os
from pathlib import Path

systemImported = True

def renameAllFiles(prefix,path,num):
    startFromNum = int(num)

    if path == "null":
        path = os.getcwd()

    if prefix == "null":
        prefix = ""

    filesList = os.listdir(str(path))

    for i in filesList:
        extension = "." + i.split(".")[len(i.split("."))-1]
        
        oldName = str(path) + "\\" + str(i)
        newName = str(path) + "\\" + prefix + str(startFromNum) + extension

        os.rename(oldName,newName)
        startFromNum += 1

    def changeFileType(path,type1,type2):
        if path == "null":
            path = os.getcwd()

        fileList = os.listdir(str(path))
        changeList = []

        for i in filesList:
            if i.split(".")[len(i.split(".")) - 1] == type1:
                changeList.append(i)
        
        for i in changeFileType:
            newType = i.split(".")[len(i.split(".")) - 1] == type2
            os.rename(i,newType)

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
if __name__ == "__main__":
    try:
        system.printLogo()
        for i in range(7):
            print("\n")
    except:
        error01("printLogo")
        
    print(color.GREEN + "This is script to rename all files in one folder.")
    print(color.GREEN + "It will rename file in alphabet order, starting with prefix of your choosing, and then number")
    print(color.GREEN + "Please, enter the prefix (null for blank):")
    prefix = input("> ")
    print(color.GREEN + "If you want to rename files in different folder, please enter path (null to rename files in same folder as this script is):")
    path = input("> ")
    print(color.GREEN + "Enter number to start from:")
    num = input("> ")
    print(color.RESET)

    renameAllFiles(prefix,path,num)
