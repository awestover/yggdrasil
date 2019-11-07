
from flask import Flask, render_template, request
from Board import Board
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/sendMove", methods=("POST",))
def handleSendMove():
    board = Board(request.form["board"])
    board.update(request.form["move"])
    computer_action = board.humanify(board.get_best_action("black"))
    board.update(computer_action)
    return json.dumps({"board": board.str_state, "move": computer_action})

if __name__ == "__main__":
    app.run(debug=True)

