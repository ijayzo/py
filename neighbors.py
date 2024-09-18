# Write your solution here
def longest_series_of_neighbours(my_list):
    neighbors = []
    new_neighbor = False 
    
    for i in range(0, len(my_list) - 1) :
        current_number = my_list[i]
        next_number = my_list[i + 1]

        if current_number - 1 == next_number or current_number + 1 == next_number :
            if i != 0 and len(neighbors) > 0 :
                last_neighbor = neighbors[len(neighbors) - 1]

                if new_neighbor :
                    neighbors.append([current_number, next_number])
                    new_neighbor = False
                
                elif last_neighbor[-1] - 1 == next_number or last_neighbor[-1] + 1 == next_number:
                    last_neighbor.append(next_number)
                else :
                    neighbors.append([current_number, next_number])
            else : 
                neighbors.append([current_number, next_number])
                new_neighbor = False
        else :
            new_neighbor = True
    longest = 0 
    for neighbor in neighbors :
        print(neighbor)
        if len(neighbor) >= longest :
            longest = len(neighbor)
    return longest # len(new)

if __name__ == "__main__" :
    #my_list = [0, 2, 4, 5, 6, 7, 10, 11, 12, 100, 101]
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
