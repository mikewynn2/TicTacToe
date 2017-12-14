import random


def display_board(board):

    print('  ' + board[1] + ' |  ' + board[2] + ' |  ' + board[3])

    print('--------------')

    print('  ' + board[4] + ' |  ' + board[5] + ' |  ' + board[6])

    print('--------------')

    print('  ' + board[7] + ' |  ' + board[8] + ' |  ' + board[9])


    pass

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1 do you want to be X or O?').upper()

    if marker == 'X':
        return('X','O')
    else:
        return('O','X')


def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or #bottomHorizontal
    (board[4] == mark and board[5] == mark and board[6] == mark) or #midHorizontal
    (board[1] == mark and board[2] == mark and board[3] == mark) or #topHorizontal
    (board[1] == mark and board[4] == mark and board[7] == mark) or #leftVertical
    (board[2] == mark and board[5] == mark and board[8] == mark) or #midVertical
    (board[3] == mark and board[6] == mark and board[9] == mark) or #rightVertical
    (board[1] == mark and board[5] == mark and board[9] == mark) or #diag1
    (board[3] == mark and board[5] == mark and board[7] == mark))   #diag2



def choose_first():
    if random.randint(1,2) == 1:
        return 'player1'
    else:
        return 'player2'


def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):

        position = input('Choose your next position: (1-9) ')
    return int(position)

def replay():
    return input('Do you want to play again? Y or N?: ').lower().startswith('y')


print('Welcome to Tic Tac Toe')

while True:

    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congrats! You won the game!')
                game_on = False

            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('DRAW!')
                    break
                else:
                    turn = 'Player 2'
        else:

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congrats! You won the game!')
                game_on = False

            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('DRAW!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break















