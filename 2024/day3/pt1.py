total = 0
with open('input.txt','r') as file:
    for line in file: 
        mulList = line.split('mul')
        for i,chunk in enumerate(mulList):
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
                    total += int(num1)*int(num2)
            

print(total)
                    
