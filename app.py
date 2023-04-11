from flask import Flask,render_template,flash,redirect,url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models.forms.loginmodel import LoginForm

app=Flask(__name__)
app.config.from_object(Config)

db=SQLAlchemy(app)
migrate=Migrate(app,db)

@app.route("/login", methods=["GET","POST"])
def login():
    formulario=LoginForm()

    if formulario.validate_on_submit():
        flash("Inicio de sesion solicitado por {}, ¿Recordarme? {}"
              .format(formulario.username.data,formulario.remember_me.data))
        return redirect(url_for('indexcss'))
    return render_template("login.html",form=formulario)

@app.route("/css")
def indexcss():
    return render_template("indexcss.html")


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

listaletras=["a","b","c"]
@app.route("/iterando")
def iterando():
    return render_template("iterando.html",letras=listaletras)

