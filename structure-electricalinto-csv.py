from locale import locale_encoding_alias
import re

def returnCredits(result):
    result=result.strip()
    if result == "A+":
        return "4.0"
    elif result == "A":
        return "4.0"
    elif result == "A-":
        return "3.7"
    elif result == "B+":
        return "3.3"
    elif result == "B":
        return "3.0"
    elif result == "B-":
        return "2.7"
    elif result == "C+":
        return "2.3"
    elif result == "C":
        return "2.0"
    elif result == "C-":
        return "1.5"
    elif result == "D":
        return "1.0"
    else:
        return "0"

writeFile=open("structure-electrical-into-csv.csv", 'w')

with open("electrical-results.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        lineList = line.split(" ")
        if len(lineList)==8:
            textToWrite=lineList[0]+","+lineList[1]+","+returnCredits(lineList[1])+"\n"+lineList[2]+","+lineList[3]+","+returnCredits(lineList[3])+"\n"+lineList[4]+","+lineList[5]+","+returnCredits(lineList[5])+"\n"+lineList[6]+","+lineList[7]+","+returnCredits(lineList[7])+"\n"
            writeFile.write(textToWrite)
        

