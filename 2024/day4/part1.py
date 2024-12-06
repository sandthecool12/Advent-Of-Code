# plus3 = 0,3,6
# plus2 = 1,3,5
# plus1 = 2,3,4
# mid = 3

xmasCounter = 0
plus3 = []
plus2 = []
plus1 =[]
# Check for diagonal and Vertical XMAS's
mid = []
with open('day4\input.txt') as txt:
    def check4Xmas (x):  
        count = 0
        if 'XMAS' in x:
            count+= x.count('XMAS')
        if 'SAMX' in x:
            count+= x.count('SAMX')
        return count
    def checkVirt(x):
        check = plus3[x]+plus2[x]+plus1[x]+mid[x]
        return check4Xmas(check)
    def checkRightDi(x):
        check = mid[x]+plus1[x+1]+plus2[x+2]+plus3[x+3]
        return check4Xmas(check)
    def checkLeftDi(x):
        check = mid[x]+plus1[x-1]+plus2[x-2]+plus3[x-3]
        return check4Xmas(check)

    for y, line in enumerate(txt):
        row = line.replace('\n',"")
        # check hori
        xmasCounter += check4Xmas(row)
        for i, letter in enumerate(row):
            mid.append(letter)
            if y>2:
                # print(y)
                xmasCounter +=checkVirt(i)
                if i<len(plus3)-3:
                    xmasCounter +=checkRightDi(i)
                if i>2:
                    xmasCounter +=checkLeftDi(i)
                    
        plus3.clear()
        plus3 = plus2.copy()
        plus2.clear()
        plus2= plus1.copy()
        plus1.clear()
        plus1 = mid.copy()
        mid.clear()
print(xmasCounter)
