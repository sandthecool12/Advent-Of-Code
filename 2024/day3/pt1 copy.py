total = 0
with open('issue1.txt','r') as file:
    for line in file: 
        print(line)
        mulList = line.split('mul(')
        print(len(mulList))
        if len(mulList[0])==0:
            mulList.pop(0)    
        print(len(mulList))    
        for chunk in mulList:
            print(chunk)
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
                    
                    total += int(num1)*int(num2)
            

print(total)
                    
