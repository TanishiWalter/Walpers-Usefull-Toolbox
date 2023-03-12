from pytube import YouTube
from colorama import Fore as color
import os

def downloadYouTubeVid(link):
    youtubeObject = YouTube(link)
    try:
        if not youtubeObject.video_id:
            return("Error, there is problem with URL.")
        else:
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            try:
                youtubeObject.download()
                return("Video downloaded")
            except:
                return("Unexpected error")
    except:
        return("Unexpected error")
    
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
    
    print("Please, input link of video that you want dto download.")
    link = input(color.GREEN + "> ")
    downloadYouTubeVid(link)