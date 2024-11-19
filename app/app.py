from flask import Flask, render_template,jsonify
from tasasBCV import traerData

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("hola.html")

@app.route('/tasasBCV') 
def tasasBCV(): 
    datos = traerData() 
    if datos: 
        return jsonify(datos) 
    else: return jsonify({"error": "No se pudieron obtener los datos"}),


if __name__ == "__main__":
    app.run(debug=True)