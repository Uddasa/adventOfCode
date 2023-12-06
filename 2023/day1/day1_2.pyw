import urllib.request
import re
import string

#logFile = open("log_day1_2.txt","w")

#url = "https://adventofcode.com/2023/day/1/input"
f = open("input_day1.txt","r")
lines = f.readlines()

p1 = re.compile('\d')

total = 0

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in lines:
    #logFile.write(line)
    firstNumber = ""
    lastNumber = ""
    firstNumberIdx = -1
    lastNumberIdx = -1
    
    firstWord = ""
    lastWord = ""
    firstWordIdx = 999999
    lastWordIdx = -1
    
    for i, c in enumerate(line):
        matches = p1.match(c)
        if (matches):
            if (firstNumber == ""):
                firstNumber = c
                firstNumberIdx = i
            lastNumber = c
            lastNumberIdx = i
        i=i+1

    #logFile.write("firstNumberIdx:" + str(firstNumberIdx) + "\n")
    #logFile.write("lastNumberIdx:" + str(lastNumberIdx) + "\n")
    idx = 0
    for number in numbers:
        #logFile.write("Search:" + number + "\n")
        idx=idx+1
        wordIdx1 = line.find(number)
        wordIdx2 = line.rfind(number)

        #if wordIdx1 != -1:
        #    logFile.write("foundFirst: " + number + " at index:" + str(wordIdx1) + "\n")

        #if wordIdx2 != -1:
        #    logFile.write("foundLast: " + number + " at index:" + str(wordIdx1) + "\n")
           
        if wordIdx1 != -1 and wordIdx1 < firstNumberIdx and wordIdx1 < firstWordIdx:
            firstWord = str(idx)
            firstWordIdx = wordIdx1
            #logFile.write("firstWord=" + firstWord + "\n")

        if wordIdx2 != -1 and wordIdx2 > lastNumberIdx and wordIdx2 > lastWordIdx:
            lastWord = str(idx)
            lastWordIdx = wordIdx2
            #logFile.write("lastWord=" + lastWord + "\n")

    first = firstNumber
    last = lastNumber
    
    if firstWord != "":
        first = firstWord

    if lastWord != "":
        last = lastWord

    #logFile.write(firstNumber + "\n")
    #logFile.write(lastNumber + "\n")
    #logFile.write(firstWord + "\n")
    #logFile.write(lastWord + "\n")
    calibration = first + last

    #logFile.write(calibration + "\n\n")
    total += int(calibration)

#logFile.write(str(total))
#logFile.close()

print(total)
  
        
        


