from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__) 

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "chave_dev_segura")
FLASK_ENV = os.getenv("FLASK_ENV", "production")

@app.route("/") 
def index():
    titulo = 'Página Inicial' 
    return render_template("index.html",titulo=titulo) # Executa o servidor SOMENTE localmente 



if __name__ == "__main__": 
    if FLASK_ENV == "desenvolvimento":
        app.run(debug=True)
    else:
        app.run(debug=False)
