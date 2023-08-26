from flask_restful import Resource, Api
from ..Modelos import db, Cancion, CancionSchema
from ..Modelos import db, Album, AlbumSchema
from ..Modelos import db, Usuario, UsuarioSchema
from flask import request

cancion_schema = CancionSchema()
album_schema = AlbumSchema()
usuario_schema = UsuarioSchema()


class VistaCanciones(Resource):
    def get(self):  # me trae todas las canciones
        global Cancion
        return [cancion_schema.dump(Cancion) for Cancion in Cancion.query.all()]

    def post(self):
        nueva_cancion = Cancion(titulo=request.json['titulo'], \
                                minutos=request.json['minutos'], \
                                segundos=request.json['segundos'], \
                                interprete=request.json['interprete'])
        db.session.add(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)  # retorna la nueva cancion en formato json


class VistaCancion(Resource):
    def get(self, id_cancion):
        return cancion_schema.dump(Cancion.query.get_or_404(id_cancion))

    # Actualizar
    def put(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        cancion.titulo = request.json.get('titulo', cancion.titulo)
        cancion.minutos = request.json.get('minutos', cancion.minutos)
        cancion.segundos = request.json.get('segundos', cancion.segundos)
        cancion.interprete = request.json.get('interprete', cancion.interprete)
        db.session.commit()
        return cancion_schema.dump(cancion)

    # Eliminacion
    def delete(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        db.session.delete(cancion)
        db.session.commit()
        return 'operacion exitosa', 204



class VistaAlbumes(Resource):
    def get(self):  # me trae todos los albumes
        global Album
        return [album_schema.dump(Album) for Album in Album.query.all()]

    def post(self):
        nuevo_album = Album(titulo=request.json['titulo'], \
                            anio=request.json['anio'], \
                            descripcion=request.json['descripcion'], \
                            medio=request.json['medio'], \
                            usuario=request.json['usuario'], \
                            canciones=request.json['canciones'], )
        db.session.add(nuevo_album)
        db.session.commit()
        return album_schema.dump(nuevo_album)  # retorna la nueva cancion en formato json

class VistaAlbumes(Resource):
    def get(self, id_album):
        return album_schema.dump(Album.query.get_or_404(id_album))

    # Actualizar
    def put(self, id_album):
        album = Album.query.get_or_404(id_album)
        album.titulo = request.json.get('titulo', album.titulo)
        album.anio = request.json.get('anio', album.anio)
        album.descripcion = request.json.get('descripcion', album.descripcion)
        album.medio = request.json.get('medio', album.medio)
        album.usuario = request.json.get('usuario', album.usuario)
        album.canciones = request.json.get('canciones', album.canciones)
        db.session.commit()
        return album_schema.dump(album)

    # Eliminacion
    def delete(self, id_album):
        cancion = Cancion.query.get_or_404(id_album)
        db.session.delete(Album)
        db.session.commit()
        return 'operacion exitosa', 204

#######################

    class VistaUsuario(Resource):
        def get(self):  # me trae todos los albumes
            global Usuario
            return [usuario_schema.dump(Usuario) for Usuario in Usuario.query.all()]

        def post(self):
            nuevo_usuario = Usuario(nombre=request.json['titulo'], \
                                    contrasena=request.json['anio'], \
                                    albumes=request.json['descripcion'],)
            db.session.add(nuevo_usuario)
            db.session.commit()
            return usuario_schema.dump(nuevo_usuario)  # retorna el usuario en formato json

    class VistaUsuario(Resource):
        def get(self, id_usuario):
            return usuario_schema.dump(Usuario.query.get_or_404(id_usuario))

        # Actualizar
        def put(self, id_usuario):
            usuario = Usuario.query.get_or_404(id_usuario)
            usuario.nombre_usuario = request.json.get('nombre', usuario.nombre_usuario)
            usuario.contrasena = request.json.get('contrasena', usuario.contrasena)
            usuario.albumes = request.json.get('albumes', usuario.albumes)
            db.session.commit()
            return usuario.dump(usuario)

        # Eliminacion
        def delete(self, id_usuario):
            usuario = Usuario.query.get_or_404(id_usuario)
            db.session.delete(Usuario)
            db.session.commit()
            return 'operacion exitosa', 204

