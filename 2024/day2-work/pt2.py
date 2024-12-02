safeCounter=0
badOnes = []
with open('input.txt','r') as file:
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
                        isIncreasing = True
                else:
                    eval = int(num) - int(numList[i-1])
                    if(isIncreasing and (eval<=0  or eval>3))or(not isIncreasing and (eval>=0 or eval<-3)):
                        isSafe = False
            return isSafe
        if numberChecker(numList):
            safeCounter+=1
        else:
            transfer = []
            for num in numList:
                transfer.append(int(num))
            badOnes.append(transfer)


        
            
            


print(safeCounter)