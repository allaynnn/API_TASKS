from flask import Flask

app = Flask(__name__)

#Ana Sehife
@app.route("/")
def home():
    return"""
<h1>Hi Everyone! My name is ALLAYN</h1>
<ul>
    <li><a href="birthday">My birthday</a></li>
    <li><a href="color">Mdevice-widthy favorite color</a></li>
    <li><a href="animal">My favorite animal</a></li>
    <li><a href="/food">My favorite food</a></li>
    <li><a href="/fruit">My favorite fruit</a></li>
</ul>
"""

#Birthday
@app.route("/birthday")
def birthday():
    return"""
<h1>Allayns birthday</h1>
<p>7 July 2005</p>
<a href="/">Back to home</a>
    """
#Color
@app.route("/color")
def color():
    return"""
<h1>My favorite color</h1>
<p>Blue</p>
<a href="/">Back to home</a>
"""

#Animal
@app.route("/animal")
def animal():
    return"""
<h1>My favorite animal</h1>
<p>Cat</p>
<a href="/">Back to home</a>
"""

#Food
@app.route("/food")
def food():
    return"""
<h1>My favorite food</h1>
<p>Plov</p> 
<a href="/">Back to home</a>
"""

#Fruit
@app.route("/fruit")
def fruit():
    return"""
<h1>My favorite fruit</h1>
<p>Watermelon</p>
<a href="/">Back to home</a>
"""
if __name__ == "__main__":
    app.run(debug=True)