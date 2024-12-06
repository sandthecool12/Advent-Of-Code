plus3 = []
plus2 = []
plus1 =[]
# Check for diagonal and Vertical XMAS's
mid = []



# x--x--x
# -x-x-x-
# --xxx--
# ---o---


# plus3 = 0,3,6
# plus2 = 1,3,5
# plus1 = 2,3,4
# mid = 3
# neg1= 2,3,4
# neg2 = 1,3,5
# negs3 = 0,3,6

xmasCounter = 0
with open('day5\input.txt') as txt:
    def check4Xmas (x):  
        count = 0
        if 'XMAS' in x:
            count+= x.count('XMAS')
        if 'SAMX' in x:
            count+= x.count('SAMX')
        return count

    # def checkVert(x):
    #     check = plus3[3]+plus2[3]+plus1[3]+mid[3]+neg1[3]+neg2[3]+neg1[3]
    #     print(x)
    def checkVirt(x):
        check = plus3[x]+plus2[x]+plus1[x]+mid[x]
        check4Xmas(check)
    def checkDi(x):
        print(x)

    row3Transfer=[]
    row2Transfer=[]    
    row1Transfer=[]
    for y, line in enumerate(txt):
        print(y)
        row = line.replace('\n',"")
        # check hori
        xmasCounter += check4Xmas(row)
        for i, letter in enumerate(row):
            if len(mid)<7:
                mid.append(letter)
                row1Transfer.append(letter)
                print(row2Transfer)
                if len(row1Transfer)>0 and y>1:
                    plus1.append(row1Transfer[i])
                if len(row2Transfer)>0 and y>2:
                    plus2.append(row2Transfer[i])
                if len(row3Transfer)>0 and y>3:
                    plus3.append(row3Transfer[i])
                if len(row3Transfer)>0:
                    checkVirt
            else:
                mid.pop(0)
                mid.append(letter)
                if len(row1Transfer)>0 and y>1:
                    plus1.pop(0)
                    print(row1Transfer)
                    plus1.append(row1Transfer[i])
                if len(row2Transfer)>0 and y>2:
                    plus2.pop(0)
                    plus2.append(row2Transfer[i])
                if len(row3Transfer)>0 and y>3:
                    plus3.pop(0)
                    plus3.append(row3Transfer[i])
                if len(row3Transfer)>0:
                    checkVirt
            
        row3Transfer.clear()
        row3Transfer = row2Transfer.copy()
        row2Transfer.clear()
        row2Transfer= row1Transfer.copy()
        row1Transfer.clear()
        mid.clear()
        print(xmasCounter)
