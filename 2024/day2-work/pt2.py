safeCounter=0
with open('input.txt','r') as file:
    # Go through each line and see if we 
    for lines in file:
        numList = lines.replace('\n','').split()
        def numberChecker(x):
            isIncreasing = True
            isSafe = True
            for i, num in enumerate(x):
                if i == 0:
                    if (int(x[1])-int(x[0]))<0:
                        isIncreasing = False
                else:
                    eval = int(num) - int(x[i-1])
                    if(isIncreasing and (eval<=0  or eval>3))or(not isIncreasing and (eval>=0 or eval<-3)):
                        isSafe = False
            return isSafe
        if numberChecker(numList):
            safeCounter+=1
        else:
            for x in range(len(numList)):
                newNumList=numList.copy()
                newNumList.pop(x)
                if numberChecker(newNumList):
                    safeCounter+=1
                    break
print(safeCounter)