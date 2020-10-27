from app import app, login_manager, db
from flask import redirect, url_for

# Rotas
from app.controllers import login
from app.controllers import corretores

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def nao_encontrado(path):
    return redirect(url_for("login"))


app.run(debug=True)
