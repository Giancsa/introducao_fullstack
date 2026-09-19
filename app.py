# importa as dependências
from flask import Flask, render_template 

#Inicializar variáveis e componentes 

#Nome do aplicativo (site web) > global
sitename = "Meu flask"

#Incializa o aplicativo Flask
app = Flask(__name__) 
 
 # Rota da pagina inicial (rota raiz ou root)
@app.route("/") 
def index(): 
    return render_template(
        "_base.html",
        sitename=sitename,
    
        )

#Rota simples
@app.route("/sobre")
def about():
    return render_template(
        "about.html",
        sitename=sitename
        )

 
#Ativa o modo DEBUG e o main loop
if __name__ == "__main__": 
    app.run(debug=True) 