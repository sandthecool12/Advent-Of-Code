
safeCounter = 0
with open('example.txt','r') as input:
    for lines in input:
        lineList = lines.replace('\n','').split(" ")
        isIncrease = True
        isSafe = True
        print(lineList)
        for i, numList in enumerate(lineList):
            num = int(numList)
            
            print(num)
            if i-1 <0:
                firstDiffrence = int(lineList[i+1])-int(lineList[i])
                if firstDiffrence <0:
                    isIncrease = False
            


                
            
            

            
        