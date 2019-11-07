
# Notes about conventions:
# black is caps
# white is lower


class Board:
    def __init__(self, init_state="NKeNPPPPppppnekn"):
        self.n = 4
        self.str_state = init_state

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
        new_state = self.str_state[:move[1]] + self.str_state[move[0]] + self.str_state[move[1]+1:]
        new_state = new_state[:move[0]] + "e" + new_state[move[0]+1:]
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

    def invert_color(self, color):
        if color == "white":
            return "black"
        elif color == "black":
            return "white"

    # returns [(start_idx, end_idx)]
    def possible_actions(self, board_state, color):
        all_possible_moves = []
        for i in range(self.n):
            for j in range(self.n):
                if self.get_piece_color(self.get_piece(i, j, board_state)) == color:
                    all_possible_moves += self.piece_possible_action(i, j, board_state)
        return all_possible_moves

    # this is the top layer of recursion
    # returns action 
    def get_best_action(self, color, max_depth=1):
        action, value = self.recursively_search_actions(self.str_state, color, max_depth)
        return action

    # this is the recursive call, it returns action, value
    def recursively_search_actions(self, board_state, color, depth_left):
        best_value = -9999999999999999999 # - inf
        best_action = (0,0)
        for action in self.possible_actions(board_state, color):
            tmp_board_state = self.test_perform_move(action)
            if depth_left == 0:
                action_value = self.board_score(tmp_board_state, color)
            else:
                opponent_action, action_value = self.recursively_search_actions(tmp_board_state, self.invert_color(color), depth_left-1)

            if action_value > best_value:
                best_value = action_value
                best_action = action
        return best_action, best_value

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
            for i_delta in (-1,0,1):
                i_new = i + i_delta
                for j_delta in (-1,0,1):
                    j_new = j_delta
                    if 0 <= i_new < self.n and 0 <= j_new < self.n:
                        possible_moves.append((self.ij_to_idx(i, j), self.ij_to_idx(i_new, j_new)))

        elif piece.lower() == "n":
            for i_delta in (-2,-1,1,2):
                i_new = i + i_delta
                for j_delta in (3-abs(i_delta), abs(i_delta)-3):
                    j_new = j + j_delta
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

