# Write your solution here
year = int(input("Year:"))
rem = year % 4
count = 4 - rem
leap = 4 + year 

jump = year + 4 - rem

if rem == 0 :
    if leap % 400 == 0 and leap % 100 == 0 :
        print (f"The next leap year after {year} is {leap}")
    elif leap % 400 != 0 and leap % 100 ==0 :
        leap += 4 
        print (f"The next leap year after {year} is {leap}")
    else :
        print (f"The next leap year after {year} is {leap}")
else :
    while True:
        count = count
        if count == 0 : 
            if jump % 400 == 0 and jump % 100 == 0 :
                print (f"The next leap year after {year} is", jump)
                break
            elif jump % 400 != 0 and jump % 100 ==0 :
                jump += 4 
                print (f"The next leap year after {year} is", jump)
                break
            else :
                print (f"The next leap year after {year} is", jump)
                break 
        else :
            count -= 1       
