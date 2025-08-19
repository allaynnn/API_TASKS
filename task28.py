from flask import Flask, render_template, request

app = Flask(__name__)

user_email = "aynurallahverdi@mail.ru"
user_password = "12345"


@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == user_email and password == user_password:
            message = f"Salam, {email}!"
        else:
            message = "Kod yanlisdir."

    return render_template("loginmail.html", message=message)
    
if __name__ == "__main__":
    app.run(debug=True)