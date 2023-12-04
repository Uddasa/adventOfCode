import urllib.request
import re
import string

#url = "https://adventofcode.com/2023/day/1/input"
f = open("input.txt","r")
lines = f.readlines()

p1 = re.compile('\d')

total = 0

for line in lines:
    first = ""
    last = ""
    for i, c in enumerate(line):
        matches = p1.match(c)
        if (matches):
            if (first == ""):
                first = c
            last = c
    calibration = first + last
    total += int(calibration)

print(total)
    
        
        


