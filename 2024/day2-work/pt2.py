safeCounter=0
with open('input.txt','r') as file:
    # Go through each line and see if its safe or if it can be safe
    for lines in file:
        numList = lines.replace('\n','').split()
        def numberChecker(x):
            isIncreasing = True
            isSafe = True
            for i, num in enumerate(x):
                # If this is the first input, check if the line should be increasing or decreasing based on the first two inputs.
                if i == 0:
                    if (int(x[1])-int(x[0]))<0:
                        isIncreasing = False
                else:
                    # For the rest of them, find what the difference between this number and the last. 
                    eval = int(num) - int(x[i-1])
                    # If it should be increasing make sure the diffrence is neither in the negatives or equal to 0 nor it is greater than 3. If so, flag it. Vice versa if it's decreasin
                    if(isIncreasing and (eval<=0  or eval>3))or(not isIncreasing and (eval>=0 or eval<-3)):
                        isSafe = False
            return isSafe
        # If it returns true, add it to the safe list
        if numberChecker(numList):
            safeCounter+=1
        else:
            # If something is wrong with the line, go through and take out one number in each line. If one of those variations come back clean, smack it with the stamp of approval and count it as safe
            for x in range(len(numList)):
                newNumList=numList.copy()
                newNumList.pop(x)
                if numberChecker(newNumList):
                    safeCounter+=1
                    break
print(safeCounter)