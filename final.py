def is_valid_move(board, row, column, direction):
    # Checks if move is valid by checking neighboring pegs.

    neighbor = "" # Peg directly next to the position peg in the desired direction. 
    otherSide = "" # Peg directly next to the neighbor peg in the desired direction.

    # Converts inputs to integers and accounts for Python indexing. 
    row = int(row) - 1
    column = int(column) - 1
    direction = int(direction)
    position = board[row][column]

    # Assigns values to neighbor and otherSide based on direction input.
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

    # Checks if move is valid.
    if position == "@" and neighbor == "@" and otherSide == "-":
        return True
    else:
        return False

def perform_move(board, row, column, direction):
    # Updates the board based on user input, only if the input is a valid move. 

    directionName = ""

    if direction == 1:
        directionName = "UP"
    elif direction == 2:
        directionName = "DOWN"
    elif direction == 3:
        directionName = "LEFT"
    elif direction == 4:
        directionName = "RIGHT"
        
    # Checks if user input is a valid move. If not, an error message is displayed and user must try again. 
    if not is_valid_move(board, row, column, direction): 
        print(f"Moving a peg from row {row} and column {column} {directionName} is not currently a legal move.")
        print()
        return False
    
    # Converts inputs to integers and accounts for Python indexing. 
    row = int(row) - 1
    column = int(column) - 1

    # Creates a copy of the board with arrays of arrays of characters instead of arrays of strings.
    newBoard = [list(row) for row in board]
    
    # Modifys board. 
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

    # Joins arrays of characters together back into a string. 
    newBoard = [''.join(row) for row in newBoard]

    return newBoard

def count_pegs_remaining(board):
    # Counts remaining pegs based on "@" in board.
    '''original
    count = 0

    for row in board:
        for i in row:
            if i == "@":
                count += 1'''

    return sum(row.count("@") for row in board)

def count_moves_available(board):
    # Tests is_valid_move() for every possible move within board.

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

    '''print(f"Possible Moves Left: {count}")'''
    return count

def read_valid_move(board):
    pass

def display_board(board):
    # Prints board for user in terminal. 
    boardString = "  "

    # Appends first line of board, the number of columns, (123...) in string
    for i in range(len(board[0])):
        boardString += str(i + 1)

    # Appends the number of rows vertically along with each row ƒrom boardArray.
    for i in range(len(board)):
        boardString += f"\n{i + 1} {board[i]}"
    
    print(boardString)

def create_board(board_type):
    # Creates board based on user input.
    board = ""
    
    # Depending on input, board variable is set equal to the string directly from Canvas website.
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

    # .split() turns the board string into an array of rows.
    boardArray = board.split()
    return boardArray 

def read_valid_int(prompt, min, max):
    # Checks if user input is a valid integer, and converts input from string to integer. 
    
    userInput = input(prompt)
    if userInput.isdigit():
        value = int(userInput)
        if value >= min and value <= max:
            return value

    # If input is not a digit within min and max, the return message prompts the user to try again.
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
    
    # User input of board type.
    board_type = read_valid_int("Choose a board style: ", 1, 4)

    print()
    # Board creation based on user input of board type.
    boardArray = create_board(board_type) 

    # Prints board for user. 
    display_board(boardArray) 

    print()
    # Loop runs until game is over. 
    while True:
        # User inputs column, row, and direction.
        column = read_valid_int("Choose the COLUMN of a peg you'd like to move: ", 1, len(boardArray[0]))
        row = read_valid_int("Choose the ROW of a peg you'd like to move: ", 1, len(boardArray))
        direction = read_valid_int("Choose a DIRECTION to move that peg 1) UP, 2) DOWN, 3) LEFT, or 4) RIGHT: ", 1, 4)

        # If the move cannot be performed, the continue keyword resets the process back to the top of the loop.
        # perform_move() includes a check for is_valid_move(). If is_valid_move returns False, then an error message occurs telling the user that their choice was invalid. 
        if not perform_move(boardArray, row, column, direction):
            continue

        # Board updates based on user input. 
        boardArray = perform_move(boardArray, row, column, direction)

        #Prints board for user. 
        display_board(boardArray)
 
        # Determins if the game is over by checking for any valid moves. 
        if count_moves_available(boardArray) == 0:
            if count_pegs_remaining(boardArray) == 1:
                print("Congrats, you won!")
            else:
                print("It looks like there are no more legal moves. Please try again.")
            break # When there are no more moves left, the while True: loop breaks regardless of a win or loss.
    
    print('''

==========================================
THANK YOU FOR PLAYING CS300 PEG SOLITAIRE!
        ''')

main()