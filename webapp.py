from flask import Flask, render_template, request, jsonify
from Expr.main import Program
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/compile", methods=["POST"])
def compile_code():
    source_code = request.form["source"]
    with open("Expr/input.txt", "w") as f_in:
        f_in.write(source_code)
    open("output.c", "w").close()
    open("exception.txt", "w").close()
    exception_msg = " "
    output_code = " "

    # try:
    prog = Program("Expr/input.txt", "output.c")
    prog.run()
    if os.path.exists("output.c"):
        with open("output.c", "r") as f_out:
            output_code = f_out.read()
    if os.path.exists("exception.txt"):
        with open("exception.txt", "r") as f_ex:
            exception_msg = f_ex.read()
    # except Exception as e:
    #     exception_msg = str(e)

    return jsonify({"output": output_code, "exception": exception_msg})


if __name__ == "__main__":
    with open("output.c", "w") as f:
        pass
    with open("exception.txt", "w") as g:
        pass
    app.run(debug=True)
