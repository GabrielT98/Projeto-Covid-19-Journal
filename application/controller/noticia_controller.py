from flask import render_template
from application.model.entity.noticia import Noticia
from application.model.DAO.estado_dao import EstadoDAO
from application import app

@app.route("/video/<int:id>")
def video(id: int):
    video = CategoriaDAO().find_video_by_id(id)
    return render_template("video.html", video=video)