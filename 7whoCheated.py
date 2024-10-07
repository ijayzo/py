import csv
from datetime import datetime, timedelta

def final_points() : 
    start = {}
    final = {}
    
    with open("start_times.csv") as start_f, open("submissions.csv") as subs :  
        for lines in csv.reader(start_f, delimiter=";") : 
            names = lines[0]
            times = datetime.strptime(lines[1], "%H:%M")
            start[names] = {
                "start_time" : times
            }

        for lines in csv.reader(subs, delimiter=";") : # name;task;points;hh:mm
            name = lines[0]
            task = lines[1]
            points = lines[2]
            time = datetime.strptime(lines[3], "%H:%M")
            if name in start :
                if time - start[name]["start_time"] > timedelta(hours=3) :
                    continue 
                if f"Task {task}" not in start[name]  :
                    start[name][f"Task {task}"] = points
                else : 
                    if start[name][f"Task {task}"] < points :
                        start[name][f"Task {task}"] = points 
    for key, value in start.items() : 
        total = 0        
        for keys, values in start[key].items() :
            if keys == "start_time" : 
                continue 
            else : 
                total += int(values)
        final[key] = total
    #print(final)
    return final

if __name__ == "__main__" : 
    final_points()

