from app import app, login_manager, db

# Rotas
from app.controllers import login
from app.controllers import corretores

app.run(debug=True)
