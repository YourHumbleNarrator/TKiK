from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/compile", methods=["POST"])
def compile_code():
    source_code = request.form["source"]
    with open("input.txt", "w") as f:
        f.write(source_code)

    subprocess.run(["python", "Expr/main.py"], check=True)

    with open("output.c", "r") as f:
        output_code = f.read()

    return jsonify({"output": output_code})

if __name__ == "__main__":
    app.run(debug=True)
