from app import db

class Salon(db.Model):
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    aula=db.Column(db.String(20))
    horaEntrada=db.Column(db.Time)
    alumno=db.relationship('Alumno',backref='salon',lazy="dynamic")