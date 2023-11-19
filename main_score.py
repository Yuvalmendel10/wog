from flask import Flask, render_template
from score import load_score

app = Flask(__name__)

@app.route('/')
def score_server():
    current_score = load_score()

    if current_score != 0:
        return render_template("score.html", score=current_score), 200
    else:
        return render_template("error.html", error = "wrong value"), 401

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=30000)