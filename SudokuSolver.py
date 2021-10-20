#v1.0
#I plan to create a visual interface next
#Studied backtracking algorithm with this program
board = [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,8],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]

def displayBo(bor):

    for i in range(len(bor)):
        if i % 3 == 0 and i != 0:
            print("*************************")
        for k in range(len(bor[0])):
            if k % 3 == 0 and k != 0:
                print(" * ",end="")
            if k == 8:
                print(str(bor[i][k]))
            else:
                print(str(bor[i][k]) + " ",end="")

def detect(borr):
    for i in range(len(borr)):
        for k in range(len(borr[0])):
            if borr[i][k] == 0:
                return(i,k)

def valider(bo,row,col,num):

    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    cor_row = row - row % 3
    cor_col = col - col % 3

    for i in range(3):
        for k in range(3):
            if bo[cor_row+i][cor_col+k] == num:
                return False
    return True

def solve(bor,row,col):

    if col == 9:
        if row == 8:
            return True #finishes
        row += 1 #proceeds to the next row
        col = 0

    if bor[row][col]>0:  #since there is a number placed, it proceeds to the next column
        return solve(bor,row,col+1)

    for num in range(1,10):

        if valider(bor,row,col,num):

            bor[row][col] = num

            if solve(bor,row,col+1):
                return True

        bor[row][col] = 0

    return False
print("Original Sudoku Board")
displayBo(board)
print("          ")
print("Solved Version")

if solve(board,0,0):
 displayBo(board)
else:
    print("No possible solution can be found. ")




