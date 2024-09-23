# Write your solution here
def dict_of_numbers():
    # Helper dictionaries
    singles = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    whole_tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
 
    numbers = {}
 
    # 0 - 9
    for i in range(10):
        numbers[i] = singles[i]
 
    # 10 - 19 are special cases
    numbers[10] = "ten"
    numbers[11] = "eleven"
    numbers[12] = "twelve"
    numbers[13] = "thirteen"
    numbers[14] = "fourteen"
    numbers[15] = "fifteen"
    numbers[16] = "sixteen"
    numbers[17] = "seventeen"
    numbers[18] = "eighteen"
    numbers[19] = "nineteen"
 
    # 20 - 99
    for i in range(2, 10):
        numbers[i * 10] = whole_tens[i]
        for j in range(1, 10):
            numbers[i * 10 + j] = whole_tens[i] + "-" + singles[j]
 
    return numbers
 
if __name__ == "__main__":
    print(dict_of_numbers())
"""
def dict_of_numbers() -> dict :
    new = {}
    nums = {}
    for i in range(0, 100) :
        if i < 20 :
            if i == 0 :
                nums[i] = "zero"
            if i == 1 :
                nums[i] = "one"
            if i == 2 :
                nums[i] = "two"
            if i == 3 :
                nums[i] = "three"
            if i == 4 :
                nums[i] = "four"
            if i == 5 :
                nums[i] = "five"
            if i == 6 :
                nums[i] = "six"
            if i == 7 :
                nums[i] = "seven"
            if i == 8 :
                nums[i] = "eight"
            if i == 9 :
                nums[i] = "nine"
            if i == 10 :
                nums[i] = "ten"
            if i == 11 :
                nums[i] = "eleven"
            if i == 12 :
                nums[i] = "twelve"
            if i == 13 :
                nums[i] = "thirteen"
            if i == 14 :
                nums[i] = "fourteen"
            if i == 15 :
                nums[i] = "fifteen"
            if i == 16 :
                nums[i] = "sixteen"
            if i == 17 :
                nums[i] = "seventeen"
            if i == 18 :
                nums[i] = "eighteen"
            if i == 19 :
                nums[i] = "nineteen"
        elif i == 20 or i == 30 or i == 40 or i == 50 or i == 60 or i == 70 or i == 80 or i == 90 : 
            if i == 20 :
                nums[i] = "twenty"
            if i == 30 :
                nums[i] = "thirty"
            if i == 40 :
                nums[i] = "forty"
            if i == 50 :
                nums[i] = "fifty"
            if i == 60 :
                nums[i] = "sixty"
            if i == 70 :
                nums[i] = "seventy"
            if i == 80 :
                nums[i] = "eighty"
            if i == 90 :
                nums[i] = "ninety"
        else : 
            if i < 30 : 
                n = i - 20
                if n < 10 :
                    if n == 1 :
                        d = "one"
                    if n == 2 :
                        d = "two"
                    if n == 3 :
                        d = "three"
                    if n == 4 :
                        d = "four"
                    if n == 5 :
                        d = "five"
                    if n == 6 :
                        d = "six"
                    if n == 7 :
                        d = "seven"
                    if n == 8 :
                        d = "eight"
                    if n == 9 :
                        d = "nine"
                    
                nums[i] = f"twenty-{d}"
            elif i < 40 : 
                n = i - 30
                if n < 10 :
                    if n == 1 :
                        d = "one"
                    if n == 2 :
                        d = "two"
                    if n == 3 :
                        d = "three"
                    if n == 4 :
                        d = "four"
                    if n == 5 :
                        d = "five"
                    if n == 6 :
                        d = "six"
                    if n == 7 :
                        d = "seven"
                    if n == 8 :
                        d = "eight"
                    if n == 9 :
                        d = "nine"
                    
                nums[i] = f"thirty-{d}"
            elif i < 50 : 
                n = i - 40
                if n < 10 :
                    if n == 1 :
                        d = "one"
                    if n == 2 :
                        d = "two"
                    if n == 3 :
                        d = "three"
                    if n == 4 :
                        d = "four"
                    if n == 5 :
                        d = "five"
                    if n == 6 :
                        d = "six"
                    if n == 7 :
                        d = "seven"
                    if n == 8 :
                        d = "eight"
                    if n == 9 :
                        d = "nine"
                    
                nums[i] = f"forty-{d}"
            elif i < 60 : 
                n = i - 50
                if n < 10 :
                    if n == 1 :
                        d = "one"
                    if n == 2 :
                        d = "two"
                    if n == 3 :
                        d = "three"
                    if n == 4 :
                        d = "four"
                    if n == 5 :
                        d = "five"
                    if n == 6 :
                        d = "six"
                    if n == 7 :
                        d = "seven"
                    if n == 8 :
                        d = "eight"
                    if n == 9 :
                        d = "nine"
                    
                nums[i] = f"fifty-{d}"
            elif i < 70 : 
                n = i - 60
                if n < 10 :
                    if n == 1 :
                        d = "one"
                    if n == 2 :
                        d = "two"
                    if n == 3 :
                        d = "three"
                    if n == 4 :
                        d = "four"
                    if n == 5 :
                        d = "five"
                    if n == 6 :
                        d = "six"
                    if n == 7 :
                        d = "seven"
                    if n == 8 :
                        d = "eight"
                    if n == 9 :
                        d = "nine"
                    
                nums[i] = f"sixty-{d}"
            elif i < 80 : 
                n = i - 70
                if n < 10 :
                    if n == 1 :
                        d = "one"
                    if n == 2 :
                        d = "two"
                    if n == 3 :
                        d = "three"
                    if n == 4 :
                        d = "four"
                    if n == 5 :
                        d = "five"
                    if n == 6 :
                        d = "six"
                    if n == 7 :
                        d = "seven"
                    if n == 8 :
                        d = "eight"
                    if n == 9 :
                        d = "nine"
                    
                nums[i] = f"seventy-{d}"
            elif i < 90 : 
                n = i - 80
                if n < 10 :
                    if n == 1 :
                        d = "one"
                    if n == 2 :
                        d = "two"
                    if n == 3 :
                        d = "three"
                    if n == 4 :
                        d = "four"
                    if n == 5 :
                        d = "five"
                    if n == 6 :
                        d = "six"
                    if n == 7 :
                        d = "seven"
                    if n == 8 :
                        d = "eight"
                    if n == 9 :
                        d = "nine"
                    
                nums[i] = f"eighty-{d}"
            elif i < 100 : 
                n = i - 90
                if n < 10 :
                    if n == 1 :
                        d = "one"
                    if n == 2 :
                        d = "two"
                    if n == 3 :
                        d = "three"
                    if n == 4 :
                        d = "four"
                    if n == 5 :
                        d = "five"
                    if n == 6 :
                        d = "six"
                    if n == 7 :
                        d = "seven"
                    if n == 8 :
                        d = "eight"
                    if n == 9 :
                        d = "nine"
                    
                nums[i] = f"ninety-{d}"
                        
    for i in range(0, 100) :
        new[i] = nums[i]

    return new 

if __name__ == "__main__" : 
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
"""
