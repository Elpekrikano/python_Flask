from flaskr import create_app
from .Modelos import db, Usuario, Album, Medio, Cancion
from .Modelos import AlbumSchema
from flask_restful import Api
from .vistas import VistaCanciones, VistaCancion


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones,'/canciones')
api.add_resource(VistaCancion,'/canciones/<int:id_cancion>')

with app.app_context():
    u = Usuario(nombre_usuario='Nicolas', contrasena='123456')
    a = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    c = Cancion(titulo='mi cancion', minutos=1, segundos=15, interprete='haaland')
    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print([AlbumSchema().dumps(album) for album in Album.query.all()])
    print(Album.query.all())
    print(Usuario.query.all()[0].albumes)
    print(Cancion.query.all())
    db.session.delete(a)
    print(Album.query.all())
    print(Cancion.query.all())
    print(Usuario.query.all())


