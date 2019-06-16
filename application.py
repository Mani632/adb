from flask import Flask,redirect,render_template,request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('Mani.html')