initialGood = []
initialBad = []
ruleBook = {}
def checkLine(x):
        errorNums={}
        printRow = []
        isValid = True
        for num in x:
            print(num)
            for previous in printRow:
                if previous in ruleBook[num]:
                    isValid=False
                    if id not in errorNums.keys():
                        errorNums[id]=[num]
                    else:
                        print(num)
                        errorNums[id].append(num)
            printRow.append(num)
            print(errorNums)
        return isValid
with open('example.txt','r') as file:
   
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
    for line in printPages:
        if checkLine(line):
            initialGood.append(line)
        else:
            initialBad.append(line)
def fixLine(x):
    print(x)

for y, badLines in initialBad:
    fixLine(badLines)
    