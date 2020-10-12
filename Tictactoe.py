def display_board(board):

    print(board[7],'|',board[8],'|',board[9])
    print(board[4],'|',board[5],'|',board[6])
    print(board[1],'|',board[2],'|',board[3])
def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input('Choose a maker X or O ')
    player1=marker
    if player1 == "x":
        player2='O'
    else :
        player2='X'
        player1='O'
        
    return (player1,player2)
def place_marker(board, marker, position):
    
    
    board[position]=marker
    
def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
import random

def choose_first():
    y=random.randint(1,2)
    if y==1:
        return 'player1'
    else:
        return 'player2'
def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False
    
def full_board_check(board):
    c=0
    for i in range(0,10):
        if space_check(board,i):
            return False
        
    return True
def player_choice(board):
    position=0
    while position not in range(0,10) or not space_check(board,position):
        position=int(input('next position b/w 1-9 : '))
    
    return position
def replay():
    again=input('do you want to play again yes or no')
    return again == 'yes'
print('Welcome to Tic Tac Toe!')

while True:
    theboard=[' ']*10
    turn = choose_first()
    player1m,player2m=player_input()
    print(turn +' will go first')
    play=input('do you want to play y or n : ')
    if play=='y':
        game_on = True
    else :
        game_on = False
    
    while game_on:
        if turn == 'player1':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player1m, position)
            
            if win_check(theboard, player1m):
                display_board(theboard)
                print('player 1 wins')
                game_on=False
            else:
                if full_board_check(theboard):
                    print("it's a draw")
                    break
                else:
                    turn='player2'
            
        else :
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player2m, position)
            
            if win_check(theboard, player2m):
                display_board(theboard)
                print('player 2 wins')
                game_on=False
            else:
                if full_board_check(theboard):
                    print("it's a draw")
                    break
                else:
                    turn='player1'
            
        
    if not replay():
        break
 # hey its not your code
