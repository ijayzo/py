def search_by_name(filename: str, word: str) : 
    name = []
    new = []
    with open(filename) as new_file : 
        for lines in new_file: 
            lines = lines.replace("\n", "")
            new.append(lines)
    for line in new : 
        if word in line.lower() : 
            if line[0] == line[0].upper() :
                name.append(line)
    return name
            

def search_by_time(filename: str, prep_time: int) : 
    time = []
    new = []
    count = 0 
    with open(filename) as new_file : 
        for lines in new_file: 
            lines = lines.replace("\n", "")
            
            if count == 0 :
                key = lines
                count += 1 
            elif count == 1 :
                value = int(lines)
                count += 1
                new.append([key, value])
            elif lines != "" :
                count += 1 
            else : 
                count = 0 
                continue  
        for i in range(0, len(new)) : 
            if new[i][1] <= prep_time :
                time.append(f"{new[i][0]}, preparation time {new[i][1]} min")    
    return time

def search_by_ingredient(filename: str, ingredient: str) : 
    new = []
    name = []
    rec = []
 
    with open(filename) as new_file : 
        new.append("")
        for lines in new_file: 
            lines = lines.replace("\n", "")
            new.append(lines)
        new.append("")

    
    for line in range(0, len(new)) : 
        up = 0
        down = 0 
        middle = line 
        forward = middle + up
        back = middle - down 
        
        if ingredient == new[line] :
            while new[line - down] != "" : 
                down += 1 
            while new[line + up] != "" : 
                up += 1 
            name.append(new[line - down + 1 : line + up ])
    print(name)
    for i in name : 
        rec.append(f"{i[0]}, preparation time {i[1]} min")    
    return rec


if __name__ == "__main__" : 
    
    found_recipes = search_by_ingredient("recipes1.txt", "tofu")

    for recipe in found_recipes:
        print(recipe)

