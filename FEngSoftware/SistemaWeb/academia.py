# Imports
from flask import Flask, render_template
from Controladores.controlador_agendamento import blue_agendamento
from Controladores.controlador_membro import blue_membro
from Controladores.controlador_atividade import blue_atividade
from Controladores.controlador_instrutor import blue_instrutor

# Gerando App Flask
app = Flask(__name__)

# Registro das Blueprints
app.register_blueprint(blue_membro)
app.register_blueprint(blue_atividade)
app.register_blueprint(blue_instrutor)
app.register_blueprint(blue_agendamento)

# Rota para a página inicial do site
@app.route('/')
def home():
    return render_template('index.html')

# Execução
if __name__ == "__main__":
    app.run(debug = True)