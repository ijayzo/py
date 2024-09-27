def read_matrix():
    with open("matrix.txt") as file:
        m = []
        for row in file:
            mrow = []
            items = row.split(",")
            for item in items:
                mrow.append(int(item))
            m.append(mrow)
 
    return m
 
# Yhdistää matriisin rivit yhdeksi listaksi
def combine(matriisi: list):
    mlist = []
    for row in matriisi:
        mlist += row
    
    return mlist
 
def matrix_sum():
    mlist = combine(read_matrix())
    return sum(mlist)
 
def matrix_max():
    mlist = combine(read_matrix())
    return max(mlist)
 
def row_sums():
    matrix = read_matrix()
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums
  """
  # write your solution here

def matrix_sum() : 
    #new = []
    s = 0
    with open("matrix.txt") as new_file : 
        for lines in new_file : #list per string = lines is list
            lines = lines.replace("\n", "")
            lines = lines.split(",") 
            #new.append(lines)
            for string in lines : 
                s += int(string)
    return s      
        
 
 
def matrix_max() : 
    s = 0
    with open("matrix.txt") as new_file : 
        for lines in new_file : #list per string = lines is list
            lines = lines.replace("\n", "")
            lines = lines.split(",")   
            for string in lines : 
                if int(string) > s :
                    s = int(string)
    return s      

def row_sums() : 
    new = []
    with open("matrix.txt") as new_file : 
        for lines in new_file : #list per string = lines is list
            s = 0
            lines = lines.replace("\n", "")
            lines = lines.split(",")   

            for string in lines : 
                s += int(string)
            new.append(s)

        return new
                          
if __name__ == "__main__" : 
    row_sums()
    matrix_sum()
    matrix_max()
"""
