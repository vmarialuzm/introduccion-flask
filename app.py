from flask import Flask,render_template

app=Flask(__name__)
#app.run(debug=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/otraRuta")
def otra_ruta():
    return "Hola, soy otra Ruta y me llamo otra ruta"

@app.route("/unaRuta")
def una_ruta():
    info="Este es un dato"
    return render_template("unaRuta.html",dato=info)
    