from flask import Flask,render_template
from application.controller import estado_controller
import os

app = Flask(__name__,template_folder=os.path.abspath('application/view/templates'),static_folder=os.path.abspath('application/view/static'))

