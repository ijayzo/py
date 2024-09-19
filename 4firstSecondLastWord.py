def first_word(strr) :
    count = 0
    index = 0
    while index < len(strr) :
        if strr[index] == " " :
            return strr[0:index]
        else : 
            index += 1

def second_word(strr) :
    count = 0
    index = 0
    ind = 0
    count2 = 0
    while index < len(strr) :
        while ind < len(strr) :
            if strr[ind] == " " : 
                count += 1
            ind += 1    

        if count == 0 :
            return 
        
        elif count == 1 :
            if strr[index] == " " :
                strr = strr[index + 1 : ]
                return strr
            else :
                index += 1
            
        else:
            if strr[index] == " " :
                count2 += 1
                if count2 == 2 :
                    return strr[place:index]
                elif count2 == 1 :
                    place = index + 1  
                    index += 1 
                else :
                    index += 1 

            else : 
                    index += 1

def last_word(strr) :
    count = 0
    index = -1
    while (-1 * index) < len(strr) :
        if strr[index] == " " :
            return strr[index + 1 : ]
            
        else : 
            index -= 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(second_word("trial and"))
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

