
totalDistance = 0
leftList = []
rightList = []

with open('input.txt', 'r') as locations:
    for lines in locations:
        twoLines = lines.replace('\n',"").split('   ')
        leftList.append(int(twoLines[0]))
        rightList.append(int(twoLines[1]))

rightList.sort()
leftList.sort()
for x in range(len(leftList)):
    lineTotal = leftList[x]-rightList[x]
    if lineTotal<0:
        lineTotal = lineTotal*-1
    totalDistance += lineTotal

print(totalDistance)
