
from glob import glob
import os
from PyPDF2 import PdfReader,PdfWriter

def getCurrentDirectory():
    print("getCurrentDirectory will be determined")
    cd = os.path.abspath(os.curdir)
    return cd

def createNewSubfolderAndGetPath(name,path):

    if isinstance(name,str) & isinstance(path,str):
        if os.path.isdir(path):
            cp = path + "/" + name +"/"
            if os.path.isdir(cp):
                status = os.path.isdir(cp)
                print("subfolder exists already")
                return cp
            else:    
                os.mkdir(cp)
                return cp

####TODO : get all pdf in current Path and print them into targetPath
def fetchPDFsAndPrint(currentPath,subFolderpath):

    if isinstance(currentPath,str) & isinstance(subFolderpath,str):
        allFilesInCurrentPath = os.listdir(currentPath)
        print(allFilesInCurrentPath)

        for file in glob("*.pdf"):
            print(file)
            filePath = str(currentPath).join(file)
            print(filePath)
            
            
            

    if __name__ == "__main__":
        cp = getCurrentDirectory()
        sfp = createNewSubfolderAndGetPath("exported",cp)

        fetchPDFsAndPrint(cp,sfp)
