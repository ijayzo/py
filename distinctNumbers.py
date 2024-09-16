def distinct_numbers(my_list) : 
    s = sorted(my_list)
    t = []

    for i in s :
        if i not in t :
            t.append(i)
    return t


if __name__ == "__main__" : 
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
