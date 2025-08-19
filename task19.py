from flask import Flask 

app = Flask(__name__)

#Ana Sehife
@app.route("/")
def home():
    return"""
<h1>Hello! Welcome to our website!</h1>
<p>Choose a page to learn more:</p>
<a href="/menu">Menu:</a><br>
<a href="/about">About:</a><br>
<a href="/contact">Contact:</a><br>
"""

#Menyu
@app.route("/menu")
def menu():
    return"""
<h1>Tickets:</h1>
<ul>
    <li>Baku-Moskow - 300 AZN</li>
    <li>Baku-Amsterdam - 550 AZN</li>
    <li>Baku-London - 400 AZN</li>
    <li>Baku-Paris - 440 AZN</li>
    <li>Baku-Ankara - 250 AZN</li>
    <li>Baku-New Dehli - 700 AZN</li>
    <li>Baku-Tbilisi - 150 AZN</li>
</ul>
<a href="/">Back</a>
    """

#Haqqimizda
@app.route("/about")
def about():
    return"""
    <h1>About:</h1>
<p>Bakidan dunyanin istenilen olkesine dogru teyyare biletlerini en munasib qiymete bizim saytimizdan elde ede bilersiniz.Size en son bilet qiymetlei haqqinda melumat vermekden memnunluq duyuruq.Ucuslarinizin rahat ve tehlukesizliyi bizim sirket terefinden qaranti olunur.Etrafli melumat ucun bizimle elaqe saxlayin.</p>
<a href="/">Back to home</a><br>
<a href="/contact">Contact</a>
 """

#Elaqe 
@app.route("/contact")
def contact():
    return"""
<h1>Contact:</h1>
<p>Bizimle elaqe saxlayin.Size xidmet etmekden memnunluq duyariq!</p>
<p>Telefon:+012827398439
<p>Email:info@informationairplane.az</p>
<a href="/">Back</a>
<a href="/">Back to home</a>
"""

if __name__ == "__main__":
    app.run(debug=True)

