
from flask import Flask, render_template, request
from Board import Board
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/doPlayerMove", methods=("POST",))
def doPlayerMove():
    board = Board(request.form["board"])
    human_action = request.form["move"]
    board.update(human_action)
    return json.dumps({"board": board.state, "move_ij": board.idx_to_ij(board.human_move_to_idxs(human_action)[1])})

@app.route("/doComputerMove", methods=("POST",))
def doComputerMove():
    board = Board(request.form["board"])
    computer_action = board.humanify(board.get_best_action("black"))
    board.update(computer_action)
    return json.dumps({"board": board.state, "move": computer_action, "move_ij": board.idx_to_ij(board.human_move_to_idxs(computer_action)[1])})

if __name__ == "__main__":
    app.run(debug=True)

