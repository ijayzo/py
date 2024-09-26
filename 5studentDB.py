# Write your solution here
def add_student(students: dict, name: str) : 
    students[f"{name}"] = []

def print_student(students: dict, name: str) : 
    is_there = False
    for key in students :
        if name == key :
            is_there = True
    if is_there == False : 
        print(f"{name}: no such person in the database")
    else :
        print(name + ":")
        if students[f"{name}"] == [] : 
            print(f"{" ":1}no completed courses")
        elif students[f"{name}"] != [] : 
            sum = 0 
            print(f"{" ":1}{len(students[name])} completed courses:")
            for i in students[name] : 
                print(f"{" ":2}{i[0]} {i[1]}")
                sum += (i[1])
            print(f"{" ":1}average grade {sum/len(students[name])}")

def add_course(students: dict, name: str, cng: tuple) : 
    if cng[1] != 0 :
        for key, value in students.items() : 
            if key == name : 
                if value == [] :
                    students[key].append(cng)
                
                else :
                    for i in range(0, len(students[key])) : 
                        if value[i][0] == cng[0] :
                            if value[i][1] < cng[1] : 
                                students[key].append(cng)
                                students[key].remove(value[i])
                        else : 
                            if value[len(students[key]) - 1][0] == cng[0] :
                                continue 
                            else : 
                                students[key].append(cng)

                

def summary (students: dict) :
    print(f"students {len(students)}")
    
    most = 0 
    name = ""
    avg = 0
    best = ""
    for key, value in students.items() : 
        ##print(len(value))
        if len(value) > most :
            most = len(value)  
            name = key
        s = 0
        for i in value : 
            s += i[1]
        
        if s / len(value) > avg : 
            avg = s / len(value)
            best = key                               
    print(f"most courses completed {most} {name}")
    print(f"best average grade {avg} {best}")


if __name__ == "__main__" : 
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
