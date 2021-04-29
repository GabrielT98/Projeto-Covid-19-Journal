from flask import Flask,render_template
import os

app = Flask(__name__,template_folder=os.path.abspath('application/view/templates'),static_folder=os.path.abspath('application/view/static'))

@app.route("/")
def home():
    return render_template("base.html")