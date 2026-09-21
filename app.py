# Importando as dependências
from flask import Flask, render_template
import sqlite3

# Inicializar variáveis e componentes

# Nome do aplicativo (Site da Web) → global
sitename = "My Flask"

# Inicializa o plaicativo Flask (HTTP)
app = Flask(__name__)

# Passa valores em comum para todas as páginas / rotas
@app.context_processor
def inject_globals():
    return {
        "sitename": sitename
    }

# Rota da página inicial (rota raiz ou root)
@app.route("/")
def index():
    return render_template(
        "home.html",
        tag_title=sitename
    )


'''
Criando páginas / rotas → Passos iniciais:
    1) Crie o template HTML em `/templates`
    2) Define a rota em `app.py`
    3) Cria a função para a rota
    4) Desenvolva a função para retornar o template HTML renderizado
'''

# Rota para '/contacts'
@app.route("/contacts", methods=['GET', 'POST'])
def contacts():
    return render_template(
        'contacts.html',
        tag_title=f"{sitename} - Faça Contato"
    )

@app.route("/about")
def about():
    return render_template(
        'about.html',
        tag_title=f"{sitename} - Sobre..."
    )


# Ativa o modo DEBUG e o main loop no localhost
if __name__ == "__main__":
    app.run(debug=True)
