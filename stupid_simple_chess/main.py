
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

def computer_action(state):
    pass


if __name__ == "__main__":
    play_computer()
    #  b = Board(init_state = "eeeeKeeeppppeeek" )
    #  b = Board(init_state = "NeeeNPPKPPppppppppppneken")
    #  __import__('ipdb').set_trace()
    #  b.show()
    #  b.get_best_action("black")
    #  print(b)
    #  print(b.get_best_action("black"))


