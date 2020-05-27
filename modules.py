from random import *


def start_board():
    startMode = integer("random board (1) or user inputted (2): ", 1, 2)
    # sanitize
    if startMode == 1:  # random board
        numRows_ = randint(8, 15)
        board_ = []
        for i in range(numRows_):
            numSticks_ = randint(7, 20)
            row_ = []
            for g in range(numSticks_):
                row_.append("|")
            board_.append(row_)

    elif startMode == 2:  # user inputted board
        numRows_ = int(input("Number of rows: "))
        board_ = []
        for i in range(numRows_):
            numSticks_ = int(input("Number of sticks in row " + str((i + 1)) + ": "))
            row_ = []
            for g in range(numSticks_):
                row_.append("|")
            board_.append(row_)

    return board_


def print_board(board_):
    print(2 * ("—" * 120 + "\n"))
    row_ = 1
    for i in board_:
        print(row_, end=": ")
        for g in i:
            print(g, end=" ")
        print("(" + str(len(i)) + ")")
        print()
        row_ += 1
    print("—" * 120 + "\n")


def remove_sticks(board_, playerTurn_):
    print(playerTurn_)
    print("What would you like to remove?")

    rowRemove_ = integer("Row: ", 1, len(board_))
    numRemove_ = integer("Number of sticks: ", 1, len(board_[rowRemove_ - 1]))

    print()

    for i in range(numRemove_):
        board_[rowRemove_ - 1].remove(board_[rowRemove_ - 1][0])
    return board_


def clean(board_):
    for i in board_:
        if len(i) == 0:
            board_.remove(i)
    return board_


def next_player(playerTurn_, player1_, player2_):
    if playerTurn_ == player1_:
        return player2_
    elif playerTurn_ == player2_:
        return player1_


def integer(prompt_, min_, max_):
    while True:
        try:
            userInput = int(input(prompt_))
        except ValueError:
            continue
        else:
            if userInput >= min_ and userInput <= max_:
                return userInput
                break


def sanitize_input(dataType_):
    if dataType_ == integer:
        pass
