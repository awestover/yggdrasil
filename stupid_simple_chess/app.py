from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/sendMove", methods=("POST",))
def handleSendMove():
    print("PLAYER MOVE: ")
    print(request.form["move"])
    return "a2a3"

if __name__ == "__main__":
    app.run(debug=True)

