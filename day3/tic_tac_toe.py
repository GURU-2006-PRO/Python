board = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

def printBoard(board):
    print(board['top-L'] + '  |' + board['top-M'] + '  |' + board['top-R'])
    print('---+---+---')
    print(board['mid-L'] + '  |' + board['mid-M'] + '  |' + board['mid-R'])
    print('---+---+---')
    print(board['low-L'] + '  |' + board['low-M'] + '  |' + board['low-R'])

def checkWin(board, player):
    return (
        (board['top-L'] == board['top-M'] == board['top-R'] == player) or
        (board['mid-L'] == board['mid-M'] == board['mid-R'] == player) or
        (board['low-L'] == board['low-M'] == board['low-R'] == player) or
        (board['top-L'] == board['mid-L'] == board['low-L'] == player) or
        (board['top-M'] == board['mid-M'] == board['low-M'] == player) or
        (board['top-R'] == board['mid-R'] == board['low-R'] == player) or
        (board['top-L'] == board['mid-M'] == board['low-R'] == player) or
        (board['top-R'] == board['mid-M'] == board['low-L'] == player)
    )

turn = 'X'
for i in range(9):
    printBoard(board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    board[move] = turn

    if checkWin(board, turn):
        printBoard(board)
        print(turn + ' has won the game!')
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
else:
    print('The game is a tie!')
