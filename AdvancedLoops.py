"""
Writing a Function that accepts 2 parameters.
Draws a playing board based on the rows and columns input
"""
def DrawingBoard(rows, columns):
    for i in range(rows):
        if i%2 == 0:
            for j in range(columns):
                if j%2 == 0:
                    if j!= columns-1:
                        print(" ",end="")
                    else:
                        print(" ")
                else:
                    if j!= columns-1:
                        print("|",end="")
                    else:
                        print("|")
        else:
            print("-"*columns)
    return True
"""
Testing out the Function
"""
DrawingBoard(23,125) 
