safeCounter=0
with open('input.txt','r') as file:
    for lines in file:
        numList = lines.replace('\n','').split()
        isSafe = True
        isIncreasing = True
        for i, num in enumerate(numList):
            if i == 0:
                if (int(numList[1])-int(numList[0]))<0:
                    isIncreasing = False
                else:
                    isIncreasing = True
            else:
                eval = int(num) - int(numList[i-1])
                if(isIncreasing and (eval<=0  or eval>3))or(not isIncreasing and (eval>=0 or eval<-3)):
                    isSafe = False
        
        if isSafe == True:
            safeCounter+=1
print(safeCounter)