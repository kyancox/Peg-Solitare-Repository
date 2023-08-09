def is_valid_move(board, row, column, direction):

    neighbor = ""
    otherSide = ""

    row = int(row) - 1
    column = int(column) - 1
    direction = int(direction)
    position = board[row][column]

    if direction == 1 and row > 1:
        neighbor = board[row - 1][column]
        otherSide = board[row - 2][column]
    elif direction == 2 and row < len(board) - 2:
        neighbor = board[row + 1][column]
        otherSide = board[row + 2][column]
    elif direction == 3 and column > 2:
        neighbor = board[row][column - 1]
        otherSide = board[row][column - 2]
    elif direction == 4 and column < len(board[0]) - 2:
        neighbor = board[row][column + 1]
        otherSide = board[row][column + 2]

    '''print(f"Position: {position}")
    print(f"neighbor: {neighbor}")
    print(f"otherSide: {otherSide}")'''

    if position == "@" and neighbor == "@" and otherSide == "-":
        return True
    else:
        return False

def perform_move(board, row, column, direction):

    directionName = ""

    if direction == 1:
        directionName = "UP"
    elif direction == 2:
        directionName = "DOWN"
    elif direction == 3:
        directionName = "LEFT"
    elif direction == 4:
        directionName = "RIGHT"
        

    if not is_valid_move(board, row, column, direction):
        print(f"Moving a peg from row {row} and column {column} {directionName} is not currently a legal move.")
        print()
        return False
    
    row = int(row) - 1
    column = int(column) - 1

    newBoard = [list(row) for row in board]
    
    if direction == 1:
        newBoard[row - 1][column] = "-"
        newBoard[row - 2][column] = "@"
    elif direction == 2:
        newBoard[row + 1][column] = "-"
        newBoard[row + 2][column] = "@"
    elif direction == 3:
        newBoard[row][column - 1] = "-"
        newBoard[row][column - 2] = "@"
    elif direction == 4:
        newBoard[row][column + 1] = "-"
        newBoard[row][column + 2] = "@"
    
    newBoard[row][column] = "-"

    newBoard = [''.join(row) for row in newBoard]

    return newBoard

def count_pegs_remaining(board):
    '''original
    count = 0

    for row in board:
        for i in row:
            if i == "@":
                count += 1'''

    return sum(row.count("@") for row in board)

def count_moves_available(board):
    
    count = 0

    for row in range(1, len(board) + 1):
        for column in range(1, len(board[0]) + 1):
            for direction in range(1,5):
                '''print(f"column: {column}")
                print(f"row: {row}")
                print(f"direction: {direction}")'''
                if is_valid_move(board, row, column, direction):
                    count += 1
                '''    print(f"count: {count}")
                else:
                    print("fail")'''

    #print(f"Possible Moves Left: {count}")
    return count

def read_valid_move(board):
    pass

def display_board(board):
    boardString = "  "

    for i in range(len(board[0])):
        boardString += str(i + 1)

    for i in range(len(board)):
        boardString += f"\n{i + 1} {board[i]}"
    
    print(boardString)

def create_board(board_type):
    board = ""

    if board_type == 1:
        board = """
		###@@@###
		###@@@###
		@@@@@@@@@
		@@@@-@@@@
		@@@@@@@@@
		###@@@###
		###@@@###"""
    elif board_type == 2:
        board = """
		#-@@-#
		-@@@@-
		@@@@@@
		@@@@@@
		-@@@@-
		#-@@-#"""
    elif board_type == 3:
        board = """
		###-@-###
		##-@@@-##
		#-@@-@@-#
		-@@@@@@@-"""
    elif board_type == 4:
        board = """
		-----
		-@@@-
		--@--
		--@--
		-----"""

    boardArray = board.split()
    return boardArray 

def read_valid_int(prompt, min, max):
    
    userInput = input(prompt)
    if userInput.isdigit():
        value = int(userInput)
        if value >= min and value <= max:
            return value

    return read_valid_int(f"Please enter your choice as an integer between {min} and {max}: ", min, max) 

def main():

    print("""
WELCOME TO CS300 PEG SOLITAIRE!
===============================

Board Style Menu
  1) Cross
  2) Circle
  3) Triangle
  4) Simple T
          """)
    
    board_type = read_valid_int("Choose a board style: ", 1, 4)

    print()
    boardArray = create_board(board_type) 

    display_board(boardArray) 

    print()
    while True:
        column = read_valid_int("Choose the COLUMN of a peg you'd like to move: ", 1, len(boardArray[0]))
        row = read_valid_int("Choose the ROW of a peg you'd like to move: ", 1, len(boardArray))
        direction = read_valid_int("Choose a DIRECTION to move that peg 1) UP, 2) DOWN, 3) LEFT, or 4) RIGHT: ", 1, 4)

        if not perform_move(boardArray, row, column, direction):
            continue

        boardArray = perform_move(boardArray, row, column, direction)

        display_board(boardArray)
 
        if count_moves_available(boardArray) == 0:
            if count_pegs_remaining(boardArray) == 1:
                print("Congrats, you won!")
            else:
                print("It looks like there are no more legal moves. Please try again.")
            break
    
    print('''

==========================================
THANK YOU FOR PLAYING CS300 PEG SOLITAIRE!
        ''')

main()