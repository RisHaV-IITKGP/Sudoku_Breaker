

# Python Code to Solve a Sudoku Puzzle using Backtracking Algorithm

# Sample Board for Testing
sample_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Input Board
board = []






# Function to Display the Sudoku Board
def display_board(bo) :

    for i in range(len(bo)) :
        if i % 3 == 0 and i != 0 :
            print("- - - - - - - - - - -")

        for j in range(len(bo[i])) :
            if j % 3 == 0 and j != 0 :
                print("|" , end = " ")

            print(bo[i][j] , end = " ")

        print()







# Function to return the first empty space in the Sudoku Board
def find_empty(bo) :

    for i in range(len(bo)) :
        for j in range(len(bo[i])) :
            if bo[i][j] == 0 :
                return (i, j)

    # If the Board is Full the return None
    return None









# Function to check if the current insertion is valid or not
# Parameters :
#              bo   ->  The current state of the Sudoku board ( After insertion )
#              num  ->  The number that has been inserted
#              pos  ->  The position where the number is inserted in the board (x, y)

def check_valid(bo , num , pos) :

    # Check for Row
    for i in range(len(bo[0])) :
        if bo[pos[0]][i] == num and i != pos[1] :
            return False

    # Check for Column
    for i in range(len(bo)) :
        if bo[i][pos[1]] == num and i != pos[0] :
            return False


    # Check for Box
    # First find the Co-ordinates of the Current Box
    x_cor = pos[0] // 3
    y_cor = pos[1] // 3

    # P.S. '//' denotes integer division

    # Now iterate over the Box
    for i in range(x_cor * 3 , x_cor * 3 + 3) :
        for j in range(y_cor * 3 , y_cor * 3 + 3) :
            if bo[i][j] == num and (i, j) != pos :
                return False


    return True










# Function to solve the Sudoku Board using Backtracking Algorithm
def solve(bo) :

    # Define the Base Case of the Recursion
    position = find_empty(bo)
    if not position :
        return True

    row, col = position

    for i in range(1,10) :
        if check_valid(bo , i , (row, col)) :
            bo[row][col] = i

            if solve(bo) :
                return True

            bo[row][col] = 0


    return False








# Function to Input the Sudoku Board from the user
def get_board() :

    try :
        for i in range(1,10) :
            a = list(map(int,input("Enter Elements of Row-" + str(i) + " : ").strip().split()))[:9]
            if len(a) != 9 :
                return False

            board.append(a)
        return True

    except :
        print("\nOof , Enter Integers !!\n")
        return False




# Driver Function
def drive() :

    print("\nEnter Elements of the Board , a Row at a Time.")
    print("Enter 0 to denote Empty Spaces.\n")
    while True :
        if get_board() :
            break

    print("\nInput Board\n")
    display_board(board)

    if solve(board) :
        print("\nSolved Board\n")
        display_board(board)
        print("\nEnjoy !!")

    else :
        print("\nSorry , This is not a valid Sudoku Board !!\n")




drive()































