
import urllib.request
import re
import string

#url = "https://adventofcode.com/2023/day/2/input"
f = open("input_day2.txt","r")
lines = f.readlines()

total = 0
totalPower = 0

# constants
maxRed = 12
maxGreen = 13
maxBlue = 14

for line in lines:
    firstSplit = line.split(":")
    gameIndexString = firstSplit[0]
    gamesString = firstSplit[1]
    
    # Find game ID
    gameId = gameIndexString.split(" ")[1]
    print("GameId="+gameId)
    
    validGame = True
    redMax = 0
    greenMax = 0
    blueMax = 0

    # Split games
    gamesSplit = gamesString.split(";")
    for game in gamesSplit:
        print(game.replace("\n", ""))
               
        # Split cubes
        cubes = game.split(",")
        for cube in cubes:
            #print(cube)
            cubeSplit = cube.split(" ")
            
            # find cube number
            cubeCount = int(cubeSplit[1])
            # find cube color
            cubeColor = cubeSplit[2].replace("\n", "")
            
            # Check validity
            if cubeColor == "red" and cubeCount > maxRed:
                validGame = False
            if cubeColor == "green" and cubeCount > maxGreen:
                validGame = False
            if cubeColor == "blue" and cubeCount > maxBlue:
                validGame = False
            
            # Get max cube count
            if cubeColor == "red" and cubeCount > redMax:
                redMax = cubeCount
            if cubeColor == "green" and cubeCount > greenMax:
                greenMax = cubeCount
            if cubeColor == "blue" and cubeCount > blueMax:
                blueMax = cubeCount
    
    power = redMax * greenMax * blueMax
    totalPower += power
        
    if validGame == True:
        print("Valid game:"+gameId)
        print("total="+str(total)+"+"+gameId)
        total += int(gameId)
        print("="+str(total)+"\n")
    else:
        print("Invalid game:"+gameId+"\n")

print(total)
print(totalPower)