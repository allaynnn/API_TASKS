from flask import Flask 
app = Flask(__name__)

# Ana Sehife 
@app.route("/")
def home():
    return """
<h1>Salam!<h1>
<p>Zehmet olmasa ozunu teqdim et: 
<p>Meselen: <a href="/My name is Allayn">/My name is Allayn</a></p>
"""
#Salamla
def salamla(ad):
    return f"""
<h1>Salam, {ad}!</h1>
<p>Welcome, nice to meet you!<p>
<a href="/">Geri qayit</a>
"""
if __name__ == "__main__":
    app.run(port=5014, debug=True)
