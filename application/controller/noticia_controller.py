from flask import render_template
from application.model.entity.noticia import Noticia
from application.model.DAO.estado_dao import EstadoDAO
from application import app

@app.route("/noticia/<int:id>")
def noticia(id: int):
    noticia = EstadoDAO().find_noticia_by_id(id)
    return render_template("noticia.html", noticia = noticia)