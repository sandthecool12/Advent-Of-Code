leftList = []
rightList = []
totalSimScore = 0
with open('input.txt', 'r') as locations:
    for lines in locations:
        twoLines = lines.replace('\n',"").split('   ')
        leftList.append(int(twoLines[0]))
        rightList.append(int(twoLines[1]))

for lNum in leftList:
    simMulti = 0
    for rNum in rightList:
        if rNum == lNum:
            simMulti+=1
    totalSimScore += simMulti*lNum
print(totalSimScore)