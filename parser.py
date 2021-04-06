import os

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

def folderScan(authorFolder, subdir=authorFolder):
    list files and directories
    for each file in files:
        if not index:
            text = parse file
            save text as file.txt in new author folder
    for each directory in directories:
        folderScan(authorFolder, directory)


for each authorDirectory in writers:
    folderScan(authorFolder)
    
