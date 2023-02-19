#This is simple script to rename all files in forlder

from colorama import Fore as color #Renamed For to color to be more readable
import os
from pathlib import Path

systemImported = True


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

#This part of script is going to be in every script in this toolbox
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