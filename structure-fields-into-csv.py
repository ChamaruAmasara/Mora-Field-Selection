
writeFile=open("fields.csv", 'w')

with open("fields-raw.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        lineList = line.split(" ")
        if len(lineList)>3:
        
            textToWrite=lineList[0]+","+lineList[-1]+"\n"
            writeFile.write(textToWrite)
    
