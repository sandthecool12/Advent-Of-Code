# plus3 = 0,3,6
# plus2 = 1,3,5
# plus1 = 2,3,4
# mid = 3

masCounter = 0
plus3 = []
plus2 = []
plus1 =[]
# Check for diagonal and Vertical XMAS's
with open('day4\input.txt') as txt:
    def check4Mas (x):  
        if 'MAS' in x or 'SAM' in x:
            return True
        else:
            return False
    def checkEven(x):
        check = plus3[x-1]+plus2[x]+plus1[x+1]
        return check4Mas(check)
    def checkOdd(x):
        check = plus3[x+1]+plus2[x]+plus1[x-1]
        return check4Mas(check)

    for y, line in enumerate(txt):
        row = line.replace('\n',"")
        for letter in row:
            plus1.append(letter) 
        for i, letter in enumerate(plus2):
            if y>1 and letter == 'A' and i>0 and i<len(plus2)-1:
                    if checkEven(i) and checkOdd(i):
                        masCounter += 1
                    
        plus3.clear()
        plus3 = plus2.copy()
        plus2.clear()
        plus2= plus1.copy()
        plus1.clear()
print(masCounter)
