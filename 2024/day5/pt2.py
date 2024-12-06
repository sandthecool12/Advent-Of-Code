counter = 0
errors = {}
fixed = []
with open('day5\input.txt','r') as file:
    ruleBook = {}
    printPages = []
    for row in file:
        line = row.replace('\n',"")
        if '|' in line:
            rule =line.split('|')
            if rule[0] not in ruleBook:
                ruleBook[rule[0]]=[rule[1]]
            else:
                ruleBook[rule[0]].append(rule[1])
        else:
            if len(line)>0:
                printPages.append(line.split(','))
    lastNum = ''
    for val in ruleBook.values():
        if len(val)==1:
            lastNum = val[0]
    ruleBook[lastNum]=[]

    for id, bind in enumerate(printPages):
        previousPages = []
        isGood = True
        for i, pNum in enumerate(bind):
            for previous in previousPages:
                if previous in ruleBook[pNum]:
                    errorNum = list(set(ruleBook[pNum])&set(previousPages))
                    for errNum in errorNum:
                        if id not in errors:
                            errors[id]={
                                'bind':bind,
                                "errNums":{errNum:[pNum]}
                                }
                        else:
                            if errNum not in errors[id]["errNums"]:
                                errors[id]["errNums"][errNum]=[pNum]
                            else:
                                errors[id]["errNums"][errNum].append(pNum)
                    isGood = False
                    # print(errors)
            previousPages.append(pNum)
    def sortBad(x):
        bind = x['bind'].copy()
        errNums = x['errNums'].copy()

        for errNum in errNums:
            print(errNum)
            bind.pop(bind.index(errNum))
            print(bind)
            for i in range(len(bind)):
                if bind[i] in ruleBook[errNum]:
                    print(f'do not skip:{bind[i]}')
                    bind.insert(i,errNum)
                    print(bind)
                    break
                if errNum in ruleBook[bind[i]]:
                    print(f'skip:{bind[i]}')
                    if i==len(bind)-1:
                        print('end')
                        bind.append(errNum)
                    continue
        return bind[int((len(bind)-1)/2)]
            
        
        
    for bad in errors.values():
        counter +=int(sortBad(bad))
print(counter)
