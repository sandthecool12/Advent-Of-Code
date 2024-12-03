total = 0
with open('input.txt','r') as file:
    for line in file:
        def multiple(x):
            tot = 0  
            mulList = x.split('mul')
            print(mulList)
            for chunk in mulList:
                if len(chunk)==0:
                    continue
                print(chunk)
                if chunk[0] == '(' and ')' in chunk:
                    num1 = ''
                    num2 =''
                    switch = False
                    addIt = True
                    multi = chunk.split(')')
                    for digi in multi[0]:
                        if digi.isnumeric() or digi == ',' or digi == '(':
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
        for do in splitDo:
            # print(do)
            if "don't()" in do:
                doList = do.split("don't()")
                # if len(doList[0]) !=0:
                total =+multiple(doList[0])
            else:
                total =+ multiple(do)

        # dont = 
        # for dontChunk in dont:
        #     do=''
        #     if "don't()" in dontChunk:
        #         do = dontChunk.split("don't()")
        #         total += multiple(do[0])
                
        #     else:
        #         total += multiple(dontChunk)

            

    
print(total)