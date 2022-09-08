from flask import Flask, jsonify, render_template, request, url_for, redirect, session, send_file
from html.parser import HTMLParser
from werkzeug.utils import secure_filename
import os, os.path
from datetime import date
import crea, envia
app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.pdf']
app.config['UPLOAD_PATH'] = 'despl-ofertas'
app.secret_key = 'esto-es-una-clave-muy-secreta'
#app.register_blueprint(base,url_prefix='-base',template_folder='templates',static_folder='static')
#app.register_blueprint(proyectos,url_prefix='-proyectos',template_folder='templates',static_folder='static')
#app.register_blueprint(unidades,url_prefix='-unidades',template_folder='templates',static_folder='static')
#app.register_blueprint(rooms,url_prefix='-rooms',template_folder='templates',static_folder='static')
#app.register_blueprint(despl,url_prefix='-despl',template_folder='templates',static_folder='static')

@app.route("/")
def hello_world():
	return redirect(url_for('login'))


@app.route("/login", methods=["POST", "GET"])
def login(message=None):
    if message == None:
        message = 'Por favor introduce tus datos'
    if request.method == 'POST':
        print("post")
        email = request.form['email']
        pwd = request.form['password']
        result = crea.checkpwd(email,pwd)
        print("result:",result)
        print(result)
        if result[0] != 'Error':
            session['nombre'] = result[1]
            session['role'] = result[0]
            return render_template('todos.html')
        else:
            message='Contraseña incorrecta'
    return render_template('login.html', message=message)

@app.route("/todos", methods=["POST", "GET"])
def correctivos():
    if session['nombre'] != None:
        return render_template('todos.html')
    else:
        return render_template('login.html', message=message)

if __name__=='__main__':
    app.run(threaded=True,host="0.0.0.0", port=5000)
