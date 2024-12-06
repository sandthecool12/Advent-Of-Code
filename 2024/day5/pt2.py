counter = 0
errors = {}
fixed = []

with open('example.txt','r') as file:
    ruleBook = {}
    def checkLine(x):
        printRow = []
        isValid = True
        for num in x:
            for previous in printRow:
                    if previous in ruleBook[num]:
                        print('yikes')
            printPages.append(x)
        return
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
    checkLine(printPages)



    # for id, bind in enumerate(printPages):
    #     previousPages = []
    #     isGood = True
    #     for i, pNum in enumerate(bind):
    #         for previous in previousPages:
    #             if previous in ruleBook[pNum]:
    #                 errorNum = list(set(ruleBook[pNum])&set(previousPages))
    #                 for errNum in errorNum:
    #                     if id not in errors:
    #                         errors[id]={
    #                             'bind':bind,
    #                             "errNums":{errNum:[pNum]}
    #                             }
    #                     else:
    #                         if errNum not in errors[id]["errNums"]:
    #                             errors[id]["errNums"][errNum]=[pNum]
    #                         else:
    #                             errors[id]["errNums"][errNum].append(pNum)
    #                 isGood = False
    #                 # print(errors)
    #         previousPages.append(pNum)




    # def sortBad(x):
        
    #     isFixed = False
        
    #     tryAgain=x.copy()

    #     while not isFixed:
    #         isGood = True
    #         bind = tryAgain['bind'].copy()
    #         errNums = tryAgain['errNums'].copy()
    #         checkBind = []
    #         print(bind)
    #         for errNum in errNums:
    #             print(errNum)
    #             bind.pop(bind.index(errNum))
    #             print(bind)
    #             for i in range(len(bind)):
    #                 if bind[i] in ruleBook[errNum]:
    #                     print(f'do not skip:{bind[i]}')
    #                     bind.insert(i,errNum)
    #                     print(bind)
    #                     break
    #                 if errNum in ruleBook[bind[i]]:
    #                     print(f'skip:{bind[i]}')
    #                     if i==len(bind)-1:
    #                         print('end')
    #                         bind.append(errNum)
    #                     continue
    #             checkBind= bind.copy()
    #         # Checking it again
    #         print(bind)
    #         for bind in checkBind:
    #             print(f'Bind:{bind}')
    #             previousPages = []
    #             isGood = True
    #             for i, pNum in enumerate(bind):
    #                 for previous in previousPages:
    #                     if previous in ruleBook[pNum]:
    #                         isGood = False
    #                 previousPages.append(pNum)
    #         if isGood:
    #             print(f'{bind} is good')
    #             isFixed=True
    #             # counter+= int(bind[int((len(bind)-1)/2)])
            


    #         # return bind[int((len(bind)-1)/2)]
            
        
        
    # for bad in errors.values():
    #     counter +=int(sortBad(bad))
print(counter)
