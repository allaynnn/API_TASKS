from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("task.html")


@app.route("/greet", methods=["POST"])
def greet():
    first = request.form.get("first_name")
    last = request.form.get("last_name")
    birthday = request.form.get("birtday_date")
    return f"<h1>Salam, {first}, {last}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
