from flask import render_template
from application.model.entity.estado import Estado
from application.model.DAO.estado_dao import EstadoDAO
from application import app

@app.route("/")
def home():
    estado_list = EstadoDAO().find_all()
    return render_template("home.html", estado_list = estado_list)
