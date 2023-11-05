import os
folderpath = r"C:\\Users\\lenik\\OneDrive\Desktop\\JELENOS\UIPATH"

def listDir(dir):
    fileNames = os.listdir(dir)
    for filename in fileNames:
        print("File Name: "+filename)
        #print("Folder Path: "+os.path.abspath(os.path.join(dir, filename)), sep="\n")

if __name__ == "__main__":
    listDir(folderpath)