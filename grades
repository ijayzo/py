# Write your solution here
def exam() -> list: 
    pElist = []
    pE = " "
    while pE != "" : 
        pE = input("Exam points and exercises completed:")
        if pE != "": 
            if pE[1] == " " :
                pElist.append(pE[0 : 1 ])
                pElist.append(pE[2 : ])
            else :     
                pElist.append(pE[0 : 2 ])
                pElist.append(pE[3 : ])
        
        
        for i in range(0, len(pElist)) : 
            if i % 2 == 0 : 
                if int(pElist[i]) < 0 and int(pElist[i]) >= 20 and int(pElist[i + 1]) < 0 and int(pElist[i + 1]) >= 100:
                    pE = ""


        
    #print("pElist")
    #print(pElist)
    
    stats(pElist)   

def stats(statsL) : 
    exP = []
    excP = []
    for i in range(0, len(statsL)) : 
        if i % 2 == 0 :
            exP.append(int(statsL[i])) 
        if i % 2 == 1 :
            fl = float(statsL[i])
            points = int(0.1 * fl)
            excP.append(points)
    print("Statistics:")
    #print("exP")
    #print(exP)
    #print("excP")
    #print(excP)
    sums(exP, excP) 

    #passing(exP)
    
    
def sums(exP, excP) : 
    sumss = []
    for i in range(0, len(exP)) : 
        sumss.append(int(exP[i]) + int(excP[i]))
    #print("sums")
    #print(sumss)
    avg(sumss)
    
    count = 0
    for i in range(0, len(exP)) : 
        if exP[i] < 10 :
            count += 1
    if count == 0 :
        gradesNoZ(sumss)
    else :
        gradesZ(exP, excP)

def avg(sumsum) : 
    count = 0
    add = 0
    while count < len(sumsum) :
        add += sumsum[count]
        count += 1 
    avg = float(add / len(sumsum))
    print(f"Points average: {avg:.1f}")

def gradesZ(l1st, l2st) : 
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    sums = []
    for i in range(0, len(l1st)) :
        if l1st[i] < 10 : 
            l1st[i] = 0
            l2st[i] = 0
            sums.append(int(l1st[i]) + int(l2st[i]))
        else :
            sums.append(int(l1st[i]) + int(l2st[i]))


    for sumss in sums : 
        if sumss <= 14 :
            zero += 1
        elif sumss <= 17 :
            one += 1
        elif sumss <= 20 :
            two += 1
        elif sumss <= 23 :
            three += 1
        elif sumss <= 27 :
            four += 1 
        else :
            five += 1 
    print(f"Pass percentage: {100* (1 - zero/len(l1st)):.1f}")
    print("Grade distribution:")
    print(f"{" ":2}5: {five * "*"}")
    print(f"{" ":2}4: {four * "*"}")
    print(f"{" ":2}3: {three * "*"}")
    print(f"{" ":2}2: {two * "*"}")
    print(f"{" ":2}1: {one * "*"}")
    print(f"{" ":2}0: {zero * "*"}")

def gradesNoZ(sumssum) : 
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    for sums in sumssum : 
        if sums <= 14 :
            zero += 1
        elif sums <= 17 :
            one += 1
        elif sums <= 20 :
            two += 1
        elif sums <= 23 :
            three += 1
        elif sums <= 27 :
            four += 1 
        else :
            five += 1 
    print(f"Pass percentage: {100 * (1 - zero/len(sumssum)):.1f}")
    print("Grade distribution:")
    print(f"{" ":2}5: {five * "*"}")
    print(f"{" ":2}4: {four * "*"}")
    print(f"{" ":2}3: {three * "*"}")
    print(f"{" ":2}2: {two * "*"}")
    print(f"{" ":2}1: {one * "*"}")
    print(f"{" ":2}0: {zero * "*"}")

def main () :
    exam()

main()
