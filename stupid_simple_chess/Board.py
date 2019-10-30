
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


