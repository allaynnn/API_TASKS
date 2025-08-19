from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def text():
    return render_template("html.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    return render_template("cavab.html", name=name, email=email)

if __name__ == "__main__":
    app.run(debug=True)