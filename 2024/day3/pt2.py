totalDo = 0
totalDont = 0
with open('input.txt','r') as file:
    for line in file:
        def multiple(x):
            tot = 0  
            mulList = x.split('mul(')
            print(len(mulList))
            if len(mulList[0]) == 0:
                mulList.pop(0) 
            print(len(mulList))
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
                        tot += int(num1)*int(num2)
            return tot
        
        splitDo = line.split('do()')
        print(splitDo[0])
        print(line)
        # totalDo += multiple(line)
        # print(line)
        for do in splitDo:
            # print('what to seperate:')
            # print(do)
            if "don't()" in do:
                doList = do.split("don't()")
                print(doList[0])
                # print('did seperate')
                # print(doList[0])
                # print(multiple(doList[0]))
                totalDont +=multiple(doList[0])
            else:
                print(do)
                # print("didnt seperate:")
                # print(do)
                # print(multiple(do))
                totalDo += multiple(do)
print(totalDo+totalDont)