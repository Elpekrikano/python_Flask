from flask import Flask
from flask import request

app = Flask(__name__)
#http://127.0.0.1:8000/params?params1=Nicolas_pachon&params2=masparametros
#http://127.0.0.1:8000
@app.route('/')
def index():
    return 'cambio por algo mas.'

@app.route('/params')
def params():
    param = request.args.get('params1', 'no hay ningun parametro') #parametros
    param_dos = request.args.get('params2', 'no hay parametro')
    return 'el parametro es : {}, {}'.format(param, param_dos)

if __name__ == '__main__':
    app.run(debug = True, port= 8000)
