
from Board import Board

def play_computer():
    board = Board()
    board.show()

    while board.notGameOver():
        print("Player turn: \n\n")

        validMove = False
        while not validMove:
            move = input("Input a move: \n")
            if board.is_valid_move(move):
                validMove = True
        board.update(move)
        board.show()

        print("Computer turn: \n\n")
        board.update(board.humanify(board.get_best_action("black")))
        board.show()

    pass

if __name__ == "__main__":
    play_computer()

