from flask import Flask

app = Flask(__name__)

#Ana Sehife
@app.route("/")
def home():
    return"""
<h1>Salam!</h1>
<p>Zehmet olmasa asagi click edin:</p>
<p>Click here:</p>
<a href="/haqqimizda">/Haqqimizda</a>
"""

#Haqqqimizda
@app.route("/haqqimizda")
def haqqinda():
    return"""
<h1>Xos gelmisiniz!</h1>
<p> Sehifemize daxil etdiyiniz melumatlar tam mexfilikle qorunmaqdadir. Her zaman xidmetinizde olmaqdan memnunluq duyariq.</p>
<p>Saytimiza daxil etdiyiniz melumatlariniza baxmaq ucun asagi hisseye click edin:</p>
<a href="/melumat">Melumatlara bax</a>
"""
#Information
@app.route("/melumat")
def information():
    return"""
<h1>Salam!</h1>
<ul>
    <li>Ad:Aynur</li>
    <li>Soyad:Allahverdiyeva</li>
    <li>Dogum Tarixi: 07.07.2005</li>
    <li>Kart nomresi:1234567890</li>
    <li>Telefon nomresi:123456789</li>
    <li>Email:@aynurallahvverdi@mail.ru</li>
    <li>FIN:1slj3Jd</li>
</ul>
<a href="/Geri Qayit"</a>
<a href="/elaqe">Elaqe</a>
"""

#Elaqe 
@app.route("/elaqe")
def contact():
    return"""
<h1>ELaqe</h1>
<p>Melumatlarda sehvlik ve deyisiklik oldugu hallarda bizimle elaqe saxlayin:
<p>Telefon:+719827398439
<p>Email:info@information.az</p>
<a href="/">Ana sehifeye qayit</a>
"""
if __name__ == "__main__":
   app.run(debug=True)