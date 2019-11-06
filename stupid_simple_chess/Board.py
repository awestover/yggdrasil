
# Notes about conventions:
# black is caps
# white is lower


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
    
    def test_perform_move(self, move):
        new_state = self.str_state
        new_state = new_state[:move[1]] + self.str_state[move[0]] + self.str_state[move[1]+1:]
        new_state = new_state[:move[0]] + "e" + self.str_state[move[0]+1:]
        return new_state

    # move is a human move
    def update(self, move): 
        start_i, start_j = self.n - int(move[1]), ord(move[0]) - ord("a")
        end_i, end_j = self.n - int(move[3]), ord(move[2]) - ord("a")
        self.modify_str_state(self.ij_to_idx(end_i, end_j), self.str_state[self.ij_to_idx(start_i, start_j)])
        self.modify_str_state(self.ij_to_idx(start_i, start_j), "e")

    # move is a computer move
    def humanify(self, move):
        ij_start = self.idx_to_ij(move[0])
        ij_end = self.idx_to_ij(move[1])
        human_ij_start = chr(ord('a') + ij_start[1]) + str(4 - ij_start[0])
        human_ij_end = chr(ord('a') + ij_end[1]) + str(4 - ij_end[0])
        return human_ij_start + human_ij_end

    def notGameOver(self):
        return True 
    def get_piece_color(self, piece):
        if piece.islower(): 
            return "white"
        else:
            return "black"

    # returns [(start_idx, end_idx)]
    def possible_actions(self, color):
        all_possible_moves = []
        for i in range(self.n):
            for j in range(self.n):
                if self.get_piece_color(self.get_piece(i, j, self.str_state)) == color:
                    all_possible_moves += self.piece_possible_action(i, j, self.str_state)
        return all_possible_moves

    def get_best_action(self, color, depth_left=3):
        best_reward = -9999999999999999999 # - inf
        best_action = (0,0)
        for action in self.possible_actions(color):
            tmp_board_state = self.test_perform_move(action)
            action_reward = self.board_score(tmp_board_state, color)
            if action_reward > best_reward:
                best_reward = action_reward
                best_action = action
        return best_action

    def ij_to_idx(self, i, j):
        return i*self.n+j

    def idx_to_ij(self, idx):
        return divmod(idx, self.n)

    def get_piece(self, i, j, board_state):
        return board_state[self.ij_to_idx(i, j)]

    # returns [(start_idx, end_idx), ...]
    def piece_possible_action(self, i, j, board_state):
        piece = self.get_piece(i, j, board_state)
        possible_moves = []
        
        if piece.lower() == "k":    
            for i_new in (-1,0,1):
                for j_new in (-1,0,1):
                    if 0 <= i_new < self.n and 0 <= j_new < self.n:
                        possible_moves.append((self.ij_to_idx(i, j), self.ij_to_idx(i_new, j_new)))

        elif piece.lower() == "n":
            for i_new in (-2,-1,1,2):
                for j_new in (3-abs(i_new), abs(i_new)-3):
                    if 0 <= i_new < self.n and 0 <= j_new < self.n:
                        possible_moves.append((self.ij_to_idx(i, j), self.ij_to_idx(i_new, j_new)))

        elif piece == "p":
            if i != 0 and self.get_piece(i-1,j,self.str_state) == "e":
                possible_moves.append((self.ij_to_idx(i, j), self.ij_to_idx(i-1, j)))
            if i != 0 and j != 0 and self.get_piece(i-1, j-1, self.str_state) != "e":
                possible_moves.append((self.ij_to_idx(i, j), self.ij_to_idx(i-1, j-1)))
            if i != 0 and j != self.n-1 and self.get_piece(i-1, j+1, self.str_state) != "e":
                possible_moves.append((self.ij_to_idx(i, j), self.ij_to_idx(i-1, j+1)))

        elif piece == "P":
            if i != self.n-1 and self.get_piece(i+1, j, self.str_state) == "e":
                possible_moves.append((self.ij_to_idx(i, j), self.ij_to_idx(i+1,j)))
            if i != self.n-1 and j != self.n-1 and self.get_piece(i+1, j+1, self.str_state) != "e":
                possible_moves.append((self.ij_to_idx(i, j), self.ij_to_idx(i+1, j+1)))
            if i != self.n-1 and j != 0 and self.get_piece(i+1, j-1, self.str_state) != "e":
                possible_moves.append((self.ij_to_idx(i, j), self.ij_to_idx(i+1, j-1)))

        non_suicidal_possible_moves = []
        for move in possible_moves:
            if self.get_piece_color(piece) != self.get_piece_color(board_state[move[1]]):
                non_suicidal_possible_moves.append(move)

        return non_suicidal_possible_moves


    def board_score(self, board_state, color):
        score = 0
        for piece in board_state:
            if self.get_piece_color(piece) == color:
                if piece.lower() == "p":
                    score += 1
                if piece.lower() == "n":
                    score += 3
                if piece.lower() == "k":
                    score += 999
            else:
                if piece.lower() == "p":
                    score -= 1
                if piece.lower() == "n":
                    score -= 3
                if piece.lower() == "k":
                    score -= 999

        return score

