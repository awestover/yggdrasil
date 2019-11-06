
class Board:
    def __init__(self):
        self.n = 4
        self.str_state = "NKeNPPPPppppnekn"
       
    def show(self):
        pictures = {"k": "♚", "K": "♔", "n": "♞",
                    "N": "♘", "p": "♟", "P": "♙", "e": " "}
        uni_str = self.str_state
        for key in pictures:
            uni_str = uni_str.replace(key, pictures[key])
        for i in range(self.n):
            for j in range(self.n*i, self.n*(i+1)):
                print(uni_str[j]+" ", end="")
            print()
           
    def is_valid_move(self, move):
        return True #not actually
   
    def modify_str_state(self, i, new_val):
        self.str_state = self.str_state[:i] + new_val + self.str_state[i+1:]
       
    def update(self, move): #move
        start_i,start_j=3-(ord(move[0])-ord("a")), int(move[1]) - 1
        end_i,end_j=3-(ord(move[2])-ord("a")),int(move[3])-1
        self.modify_str_state(4*end_i + end_j, self.str_state[4*start_i + start_j])
        self.modify_str_state(4*start_i + start_j, "e")

    def notGameOver(self):
        return True


    def ij_to_idx(self, i, j):
        return i*self.n+j

    def get_piece(self, i, j):
        return self.str_state[self.ij_to_idx(i, j)]

    # returns (start_idx, end_idx)
    def piece_possible_action(self, i, j):
        piece = self.get_piece(i, j)
        possible_moves = []

        if piece.lower() == "k":    
            for i_new in (-1,0,1):
                for j_new in (-1,0,1):
                    if 0 <= i_new < self.n and 0 <= j_new < self.n:
                        possible_moves.append(self.ij_to_idx(i, j), self.ij_to_idx(i_new, j_new))

        elif piece.lower() == "n":
            for i_new in (-2,-1,1,2):
                for j_new in (3-abs(i_new), abs(i_new)-3):
                    if 0 <= i_new < self.n and 0 <= j_new < self.n:
                        possible_moves.append(self.ij_to_idx(i, j), self.ij_to_idx(i_new, j_new))

        elif piece == "p":
            if i != 0:
                possible_moves.append(i-1, j)
            if self.get_piece(i-1, j-1) != "e":
                possible_moves.append(self.ij_to_idx(i-1, j-1))

        elif piece == "P":
            if i != self.n:
                possible_moves.append(i+1, j)
            if self.get_piece(i+1, j+1) != "e":
                possible_moves.append(self.ij_to_idx(i+1, j+1))

        return possible_moves
                