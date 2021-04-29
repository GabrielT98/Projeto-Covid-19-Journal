from flask import Flask

app = Flask(__name__,template_folder=os.path.abspath('application/view/templates'),static_folder=os.path.abspath('application/view/static'))