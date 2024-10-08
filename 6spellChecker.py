# my solution here, "model solution at end" (more memory?)
last = []
line = input("write text: ")
normline = line.split(" ")

lowline = line.lower()
words = lowline.split(" ")

for i in range(0, len(words)) : 
    with open("wordlist.txt") as new_file :
        for lines in new_file : 
            lines = lines.replace("\n", "")            
            if lines != words[i] :  
                continue 
            else : 
                last.append(normline[i])
                break
for i in range(0,len(normline)) :
    if normline[i] in last : 
    
        if i < len(normline) - 1 : 
            print(normline[i], end=" ")
        else : 
            print(normline[i])
    else : 
        if i < len(normline) - 1 : 
            print(f"*{normline[i]}*", end=" ")
        else : 
            print(f"*{normline[i]}*")

--------------
def wordlist():
    words = []
 
    with open("wordlist.txt") as file:
        for row in file:
            words.append(row.strip())
 
    return words
 
words = wordlist()
sentence = input("Write text: ")
 
for word in sentence.split(' '):
    if word.lower() in words:
        print(word + " ", end="")
    else:
        print("*" + word + "* ", end="")
 
print()
