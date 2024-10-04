# Write your solution here
with open("dictionary.txt") as my_file:
    for lines in my_file :
        lines = lines.replace("\n", "")
boole = True 
dicti = []
while boole : 
    print("1 - Add word, 2 - Search, 3 - Quit")
    fu = int(input("Function: "))
    if fu == 3 : 
        boole == False
        print("Bye!") 
        break 
    elif fu == 2 : 
        se = input("Search term: ")
        with open("dictionary.txt") as new_file : 
            for lines in new_file: 
                lines = lines.replace("\n", "")
                lines = lines.split(" - ")
                if se in lines[0] :
                    print(f"{lines[0]} - {lines[1]}")
                if se in lines[1] :    
                    print(f"{lines[0]} - {lines[1]}")
                    
    else : 
        fi = input("The word in Finnish: ")
        en = input("The word in English: ")  
        f = [fi, en]
        dicti.append(f)
        with open("dictionary.txt", "a") as new_file : 
            new_file.write(f"{fi} - {en}\n")
        print("Dictionary entry added")
    
