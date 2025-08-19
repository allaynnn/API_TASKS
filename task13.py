from flask import Flask

app = Flask(__name__)

#Ana Sehife:
@app.route("/")
def home():
    return """
    <h1>Welcome to Allayn's Restaurant!</h1>
    <p>Choose a page to learn more.</p>
    <a href ="/menu">Menyu</a><br>
    <a href="/about">Haqqimizda</a><br>
    <a href="/contact">Elaqe</a> 
    """
#Menyu:
@app.route("/menu")
def menu():
    return"""
    <h1>Menu:</h1
    <ul>
        <li>Plov - 10 AZN</li>
        <li>Kabab - 20 AZN</li>
        <li>Dolma - 15 manat</li>
        <li>Shah Plov - 30 manat</li>
        <li>Dovga - 8 manat</li>
    </ul>
    <a href="/">Geri Qayit</a>
    """
#Haqqimizda:
@app.route("/about")
def about():
    return"""
    <h1>Haqqimizda:</h1>
    <p>We prepare the most delicious Azerbaijani dishes.</p>
    <a href="/">Geri</a>
    """
#Elaqe:
@app.route("/contact")
def contact():
    return"""
    <h1>Elaqe:</h1>
    <p>Email: info@allaynsrestaurant.az</p>
    <p>Telefon: 123456789</p>
    <a href="/">Geri</a>
    """

if __name__=="__main__":
    app.run(debug=True)
    
