from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class AlumnoForm(FlaskForm):
    id=StringField("ID de Alumno",validators=[DataRequired()])
    nombre=StringField("Nombre de Alumno",validators=[DataRequired()])
    apellido=StringField("Apellido de Alumno",validators=[DataRequired()])
    