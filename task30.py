from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def my_task(): 
    return render_template ("mytask.html")

@app.route("/age", methods=["POST"])
def age ():
    name = request.form.get("name")
    age = request.form.get("age")

    return render_template ("age.html", name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)