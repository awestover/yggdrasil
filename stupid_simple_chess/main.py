
from Board import Board

def play_computer():
    board = Board()

    while board.notGameOver():
        board.show()
        print("Player turn: \n\n")

        validMove = False
        while not validMove:
            move = input("Input a move: \n")
            if board.is_valid_move(move):
                validMove = True
        
        board.update(move)

        print("Computer turn: \n\n")
        computer_action(board.str_state)

    pass

def computer_action(state):
    pass


if __name__ == "__main__":
    play_computer()

