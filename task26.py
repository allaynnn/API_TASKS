from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def age_calculator():
    age = None
    if request.method == "POST":
        dob_str = request.form.get("dob")
        if dob_str:
            dob = datetime.strptime(dob_str, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    return render_template("allayn.html", age=age)

if __name__ == "__main__":
    app.run(debug=True)
