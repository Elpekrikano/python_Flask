from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cancion(db.Model):
    _tablename_='Cancion'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))

class Usuario(db.Model):
    _tablename_='Usuario'
    id= db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(128))
    contrasena= db.Column(db.String(128))

class Album(db.Model):
    _tablename_ = 'Album'
    id=db.Column(db.Integer, primary_key=True)
    titulo=db.Column(db.String(128))
    año=db.Column(db.Integer)
    descripcion=db.Column(db.String(128))
    medio=db.Column(db.Enum('DISCO','CASETE','CD'))

    #Medios: DISCO, CASETE, CD