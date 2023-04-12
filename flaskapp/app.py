import os
from flask import Flask,render_template,flash,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models.forms.loginmodel import LoginForm
from models.forms.alumnoform import AlumnoForm
from models.forms.salonform import SalonForm

app=Flask(__name__)
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('SQLALCHEMY_DATABASE_URI')

Bootstrap(app)

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

@app.route("/registrar", methods=["GET","POST"])
def registrar():
    
    alumnoForm=AlumnoForm()
    salonForm=SalonForm()

    if salonForm.validate_on_submit():
        from models.db.salonmodel import Salon
        from models.db.alumnomodel import Alumno

        s1=Salon(aula=salonForm.aula.data,horaEntrada=salonForm.horaEntrada.data)
        a1=Alumno(id=int(alumnoForm.id.data),nombre=alumnoForm.nombre.data,apellido=alumnoForm.apellido.data,salon=s1)

        db.session.add(s1)
        db.session.add(a1)

        db.session.commit()

        return redirect(url_for('registrar'))


    return render_template("registrar.html",formAl=alumnoForm,formSa=salonForm)

    
#funcion para insertar manualmente los datos en los modelos
def insert_record():
    from models.db.salonmodel import Salon
    from models.db.alumnomodel import Alumno

    s1=Salon(aula="Z",horaEntrada="10:30")
    a1=Alumno(id=25,nombre="Marcelo",apellido="Salas",salon=s1)

    db.session.add(s1)
    db.session.add(a1)

    db.session.commit()

@app.route("/")
def index():

    #insertar_record()

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

    from models.db.alumnomodel import Alumno

    alumnos=Alumno.query.all()
    lista_alumno=[]
    for alumno in alumnos:
        lista_alumno.append(alumno)

    return render_template("iterando.html",letras=lista_alumno)

