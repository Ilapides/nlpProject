import re
import os
from bs4 import BeautifulSoup




# parser must do the following:
# extract text from html
# cut off header
# cut off footer (footnotes etc.)

''' navigation:
home folder: writers
then for each author:
for a given directory tree:
    ignore index
    open each html file and get text
    save in single authop

aka
'''
def parser(fileName):
    html = open(fileName, "rb")
    soup = BeautifulSoup(html).text
    html.close()
    startIndex = soup.find("On-Line (ETOL).") + 15
    endIndex = soup.find("Top of page")
    return soup[startIndex:endIndex]



def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        if entry == "index.html":
            continue
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles


def main():  
    dirName = '/home/isaac/NLP/writers/'
    authors = os.listdir(dirName)
    for author in authors:
        authorDirName = dirName + author
        listOfFiles = getListOfFiles(authorDirName)
        authorFile = open("writers/" + author + ".txt", "w")
        for f in listOfFiles:
            print(f)
            filetext = parser(f)
            authorFile.write(filetext + "\n")
        authorFile.close()
    # x = parser("/home/isaac/NLP/writers/mcshane/1980/05/marx.html")
    # with open("mcshane", "w") as mcsh:
    #     mcsh.write(x)

    

if __name__ == '__main__':
    main()