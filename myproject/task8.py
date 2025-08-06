from flask import Flask 
app = Flask(__name__)

#Ana Sehife
@app.route("/")
def home():
    return """
    <h1>Ana Sehife</h1>
    <p>Salam, xos gelmisen!<p>
    <a href="/haqqinda">Haqqimda</a><br>
    <a href="/elaqe">Elaqe</a>
    """
#Haqqinda hissesi
@app.route("/haqqinda")
def haqqinda():
    return """
    <h1> Haqqimda</h1>
    <p> My name is AllAyn. I'm learning Flask and this is my first site!<p>
    <a href="/">Geri qayit</a>
    """
#Elaqe hissesi
@app.route("/elaqe")
def elaqe():
    return """
    <h1>Elaqe</h1>
    <p>Email:allayn@me.com<p>
    <a href="/">Geri qayit</a>
    """


if __name__ == "__main__":
    app.run(debug=True)
        
