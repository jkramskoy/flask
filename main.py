from flask import Flask,render_template
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello visitor!Nice to see you on my website! "

@app.route("/about")
def about_me():
    return "I am a SmartNinja student.This is my Fakebook website"

@app.route("/portfolio")
def portfolio():
    return render_template("index.html")

@app.route("/portfolio/fakebook")
def fakebook():
    return redirect('http://localhost:63342/Fakebook/Fakebook.html?_ijt=ppqhta6tljdmc9agperd2umsvm')

@app.route("/portfolio/boogle")
def boogle():
    return redirect('http://localhost:63342/boogle_login/boogle_login.html?_ijt=ppqhta6tljdmc9agperd2umsvm')

@app.route("/portfolio/hair-salon")
def hair_salon():
    return redirect('http://localhost:63342/hair_salon/index.html?_ijt=ppqhta6tljdmc9agperd2umsvm')



if __name__ == '__main__':
    app.run(port="5004")

