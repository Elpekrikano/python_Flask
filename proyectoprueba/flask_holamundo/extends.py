from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def user(name='Bienvenido'):
    age = 20
    my_list = [1,2,3,4,5,6]
    return render_template('user.html', name=name, age=age, list=my_list)

@app.route('/user/<name>')
def user2(name='Nicolas'):
    age = 20
    my_list = [7,8,9,10,11,12]
    return render_template('user2.html', name=name, age=age, list=my_list)

if __name__ == '__main__':
    app.run(debug = True, port= 8000)