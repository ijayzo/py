# Write your solution here
def print_sudoku(sudoku: list) : 
    for row in range(0, 9) : 
        for col in range(0, 9) : 
            if sudoku[row][col] == 0 :
                print("_", end="")
                if col == 2 or col == 5 :
                    print("  ", end="")
                elif col == 8 : 
                    print()
                else : 
                    print(" ", end="")
            elif sudoku[row][col] > 0 :
                print(f"{sudoku[row][col]}", end="")
                if col == 2 or col == 5 :
                    print("  ", end="")
                elif col == 8 : 
                    print()
                else : 
                    print(" ", end="")

        if row == 2 or row == 5 : 
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) :
    new = sudoku[:]
    new[row_no][column_no] = number
    return new

if __name__ == "__main__" :
    sudoku  = [
    [0, 1, 2, 3, 4, 5, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    grid_copy = copy_and_add(sudoku, 0, 0, 2)

    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
