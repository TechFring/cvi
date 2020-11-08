from app import app, login_manager, db
from flask import redirect, url_for

# Rotas
from app.controllers import login
from app.controllers import corretores
from app.controllers import imoveis


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def nao_encontrado(path):
    return redirect(url_for("login"))


app.run(debug=True)
