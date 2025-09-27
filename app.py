from flask import Flask, render_template 
app = Flask(__name__) 
@app.route("/") 


def index():
    titulo = 'Página Inicial' 
    return render_template("index.html",titulo=titulo) # Executa o servidor SOMENTE localmente 





if __name__ == "__main__": app.run(debug=True)