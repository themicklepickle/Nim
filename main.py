from nim_v2_modules import *

player1 = input("Player 1: ")
player2 = input("Player 2: ")

playAgain = True

while playAgain == True:

    board = startBoard()

    playerTurn = player2

    while len(board) > 0:

        playerTurn = nextPlayer(playerTurn, player1, player2)

        board = clean(board)
        print_board(board)

        board = clean(board)
        board = remove_sticks(board, playerTurn)

        board = clean(board)

    print(playerTurn, "wins!!!")

    playAgain = integer("Play again? Yes (1) or No (2): ", 1, 2)