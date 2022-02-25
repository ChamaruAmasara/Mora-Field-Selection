from locale import locale_encoding_alias
import re



writeFile=open("E5-list-into-csv.csv", 'w')

with open("E5-list.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        lineList = line.split(" ")
        if len(lineList)>=3:
            textToWrite=lineList[0]+","+lineList[1]+" "+lineList[2]+"\n"
            writeFile.write(textToWrite)
        else:
            print(lineList)
        

