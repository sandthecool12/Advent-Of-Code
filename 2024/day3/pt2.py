totalDo = 0
isDo=True
with open('input.txt','r') as file:
    
    for line in file:
        # This takes the given of data, splits it into chunks to be evaluated. If it is clean, take the numbers inside the data and multiply it.
        def multiple(x):
            tot = 0  
            mulList = x.split('mul(')
            # If it starts with 'mul(' then it throws an error because it splits it and the first index is blank. This takes it out of the equation.
            if len(mulList[0]) == 0:
                mulList.pop(0) 
            for chunk in mulList:
                if chunk[0].isnumeric() and ')' in chunk:
                    num1 = ''
                    num2 =''
                    switch = False
                    addIt = True
                    multi = chunk.split(')')
                    for digi in multi[0]:
                        if digi.isnumeric() or digi == ',':
                            if digi ==",":
                                switch = True
                            elif switch and digi.isnumeric():
                                num2+=digi
                            elif digi.isnumeric():
                                num1+=digi
                        else:
                            addIt=False
                            break
                    if addIt:
                        print(chunk)
                        tot += int(num1)*int(num2)
            return tot
        # Take the data and split them into do chunks.
        splitDo = line.split('do()')
        # Go through the do chunks, if you find a don't(), cut it off and only evaluate the part before
        for i,do in enumerate(splitDo):
            isLast = len(splitDo)-1==i
            if not isDo and i==0:
                continue
            if "don't()" in do:
                if isLast:
                     isDo=False
                doList = do.split("don't()")
                totalDo +=multiple(doList[0])
            else:
                if isLast:
                     isDo=True
                totalDo += multiple(do)
print(totalDo)
