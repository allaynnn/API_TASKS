from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    username = request.form.get("username")  # Formadan adı alırıq
    return f"<h1>Salam, {username}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
