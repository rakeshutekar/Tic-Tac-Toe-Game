import os
import random
def clear():
    os.system( 'cls' )
    

def display_board(board): # Create a board to play tic tac toe using print functions.
    clear()
    print('   |   |  ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('---|---|---  ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('---|---|---  ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('   |   |  ')
    


def player_input():
    marker=''
    while not (marker =='O'  or marker =='X'):
        marker = input("Player 1:Do you want to be X or O\n").upper()
        
    if marker == 'X': # Check if input is 'X'.
        return ('X', 'O') # Return a tuple.
    else: # Use else instead of elif marker == 'O' since there are only two possible correct inputs.
        return ('O', 'X')     


def place_marker(board,marker,position):
     board[position]= marker

def win_check(board,mark): # Checks if either player won the game.
#Check to see if there is a winning line...
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top.
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle.
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom.
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side.
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle.
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side.
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonally.
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonally.

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
      return board[position] == ' '

def full_board_check(board):
      for i in range(1,10):
           if space_check(board,i):
               return False
      return True     
        

def player_choice(board):
    position = '  '
    while  position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
           position = input('Choose your next position: (1-9) ')
    return int(position)

def replay():
  return input('Do you want to play again? Enter Yes or No ').lower().startswith('y')
    
           
print ("**********Welcome to Tic Tac Toe!*************")     
while True:

    theboard =[' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + "will go first!")
    game_on = True

    while game_on :
        
        if turn == "Player 1":
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard,player1_marker,position)

            if win_check(theboard,player1_marker):
                 display_board(theboard)
                 print("Congratulations,Player 1, has won the game")
                 game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("The game is draw!")
                    break
                else:
                    turn = "Player 2"
        
        else:                           # Initialize the Player 2's turn
            display_board(theboard)             # Display the board
            position = player_choice(theboard)              # Position of player's move is checked using player_choice function 
            place_marker(theboard, player2_marker, position)          # Place the marker on the board using player's marker(X or O) and place
                                                                      # in position

            if win_check(theboard,player2_marker): # Check if Player 1 has won the game.
                display_board(theboard) # Pass theBoard into function display_board to check if there is a line that wins on board.
                print('Congratulations, Player 2 has won the game!')
            else:
                if full_board_check(theboard): # Check if board is full.
                    display_board(theboard) # Pass the game board into the display_board function to see if board is full.
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
     break  
