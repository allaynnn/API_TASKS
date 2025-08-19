from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Xoş gəlmisiniz! Rəng seçmək üçün <a href='/color'>buraya klikləyin</a>."


@app.route("/color", methods=["GET", "POST"])
def color():
    if request.method == "POST":
        my_favorite_color = request.form.get("my_favorite_color")
        return render_template ("color_result.html", color=my_favorite_color)
    return render_template("color_form.html")

if __name__ == "__main__":
    app.run(debug=True)