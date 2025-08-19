from flask import Flask

app = Flask(__name__)

#Ana Sehife
@app.route("/")
def home():
    return"""
<h1>SALAM!</h1>
<p>Saytimiza xos gelmisiniz!</p>
<p>Etrafli melumat ucun click edin:</p>
<a href="/haqqimizda">About</a><br>
<a href="/elaqe">Contact</a><br>
<a href="menyu">Menyu</a><br>
"""

#Menyu
@app.route("/menyu")
def menu():
    return"""
<h1>Biletler:</h1>
<ul>
    <li>Baki-Siyezen - 3.60 AZN</li>
    <li>Baki-Imisli - 15 AZN</li>
    <li>Baki-Gence - 20 AZN</li>
    <li>Baki-Kurdemir - 8 AZN</li>
    <li>Baki-Qazax - 9 AZN</li>
    <li>Baki-Naxcivan - 20 AZN</li>
    <li>Baki-Agcabedi - 7.50 AZN</li>
</ul>
<a href="/">Geri Qayit</a>
    """

#Haqqimizda:
@app.route("/haqqimizda")
def about():
    return"""
<h1>Haqqimizda</h1>
<p>Olkedaxili biletleri bizim saytimizda en uygun qiymete tapa bilersiniz.Xidmetinizde durmaga her zaman haziriq.Etrafli melumat ucun bizimle elaqe saxlayin:)<p>
<a href="/">Ana sehifeye geri qayit</a><br>
<a href="/elaqe">Elaqe</a>
"""

#Elaqe:
@app.route("/elaqe")
def elaqe():
    return"""
<h1>Elaqe:</h1>
<p>Bizimle elaqe saxlayin.Size xidmet etmekden memnunluq duyariq!</p>
<p>Telefon:+012827398439
<p>Email:info@avtovagzalbiletleri.az</p>
<a href="/">Geri</a>
<a href="/">Ana sehifeye qayit</a>
"""

if __name__ == "__main__":
    app.run(debug=True)
