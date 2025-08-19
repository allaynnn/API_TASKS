from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            forecast = f"<h2>{city} şəhərində sabah günəşli olacaq! ☀️</h2>"
        else:
            forecast = ""
    else:
        forecast = ""

    return f"""
    <html>
        <head>
            <title>Hava Proqnozu</title>
        </head>
        <body>
            <h1>Sadə Hava Proqnozu</h1>
            <form method="POST">
                <label>Şəhər adı:</label><br>
                <input type="text" name="city" required><br><br>
                <button type="submit">Proqnozu göstər</button>
            </form>
            {forecast}
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
