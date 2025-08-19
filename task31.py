from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def qiymet():
    return render_template("qiymet.html")

@app.route("/rate", methods=["POST"])
def rate():
    name = request.form.get("name")
    rating = request.form.get("rating")
    return render_template("rate.html", name=name, rating=rating)

if __name__ == "__main__":
    app.run(debug=True)