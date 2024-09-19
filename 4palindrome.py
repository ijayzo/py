def palindromes(word: str):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
            return False
    return True
 
while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        print(word, "is a palindrome!")
        break
    print("that wasn't a palindrome")


---
# or 

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
