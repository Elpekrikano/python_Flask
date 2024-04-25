from flask import Flask

#servidor/cliente

app = Flask(__name__)#numevo objeto,

#ruta o decorador wrap
@app.route('/')
def index():
    return 'hola mundo' #Regresar un string


app.run()#ejecuta el servidor 5000
