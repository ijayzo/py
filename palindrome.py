def palindromes(str1) :
    return str1 == str1[::-1]
str1 = "  "
while len(str1) > 1 :
    str1 = input("Please type in a palindrome:")
    if palindromes(str1) == True :
        print(f"{str1} is a palindrome!")
        break
    else : 
        print("that wasn't a palindrome")
