#This is script to combine 2 PDFs into one
import os
import PyPDF2
from colorama import Fore as color

def combineTwoPdfs(path1,path2):
    pdf1 = open(path1,"rb")
    pdfReader1 = PyPDF2.PdfFileReader(pdf1)

    pdf2 = open(path2,"rb")
    pdfReader2 = PyPDF2.PdfFileReader(pdf2)

    pdfWriter = PyPDF2.PdfFileWriter()

    for page_num in range(pdfReader1.numPages):
        page = pdfReader1.getPage(page_num)
        pdfWriter.addPage(page)
    
    for page_num in range(pdfReader2.numPages):
        page = pdfReader2.getPage(page_num)
        pdfWriter.addPage(page)

    pdfOutput = open('combined.pdf', 'wb')
    pdfWriter.write(pdfOutput)

    pdfOutput.close()
    pdf1.close()
    pdf2.close()
        
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

    print(color.GREEN + "This is Python script that combines two PDFs into one.")
    print("Please, tipe in first path of your PDFs:")
    path1 = input("> ")
    print("Now input the other path: ")
    path2 = input("> ")
    print(color.RESET)

    combineTwoPdfs(path1,path2)



    

    