counter = 0
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

    for bind in printPages:
        print(f'Bind:{bind}')
        previousPages = []
        isGood = True
        for i, pNum in enumerate(bind):
            for previous in previousPages:
                if previous in ruleBook[pNum]:
                    isGood = False
            previousPages.append(pNum)
        if isGood:
            counter+= int(bind[int((len(bind)-1)/2)])
    
    
print(counter)
