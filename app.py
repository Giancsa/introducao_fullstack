# importa as dependências
from flask import Flask 

#Inicializar variáveis e componentes 

#Incializa o aplicativo Flask
app = Flask(__name__) 
 
 # Rota da pagina inicial (rota raiz ou root)
@app.route("/") 
def hello_world(): 
    return "<p>Hello, World!</p>"

#Rota simples
@app.route("/about")
def about():
    output= "Sobre nós..."
    return output 

 
#Ativa o modo DEBUG e o main loop
if __name__ == "__main__": 
    app.run(debug=True) 