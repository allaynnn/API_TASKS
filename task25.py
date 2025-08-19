from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("rating.html")

@app.route("/rate", methods=["POST"])
def rate():
    rating = request.form.get("rating")
    if rating:
        return f"<h1>Sayti {rating} bal ile qiymetlendirdiyiniz ucn tesekkur edirik!</h1>"
    else:
        return f"<h1>Zehmet olmasa bir qiymet secin:</h1>"
    
    
    
if __name__ == "__main__":
    app.run(debug=True)