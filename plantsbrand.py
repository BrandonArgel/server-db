from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL, MySQLdb
from flask_bcrypt import bcrypt
brandplantsApp = Flask(__name__)
brandplantsApp.config['MYSQL_HOST'] = 'localhost'
brandplantsApp.config['MYSQL_USER'] = 'root'
brandplantsApp.config['MYSQL_PASSWORD'] = 'mysql'
brandplantsApp.config['MYSQL_DB'] = 'plantsbrand'
brandplantsApp.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(brandplantsApp)
@brandplantsApp.route('/')
def index():
    return render_template('inicio.html')
    
@brandplantsApp.route('/login')
def login():
    return render_template('login.html')

@brandplantsApp.route('/registro', methods = ['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombrec = request.form['nombrec']
        correoc = request.form['correoc']
        clavec = request.form['clavec'].encode('utf-8')
        clavecifrada = bcrypt.hashpw(clavec, bcrypt.gensalt())
        regcliente = mysql.connection.cursor()
        regcliente.execute("INSERT INTO cliente (nombrec, correoc, clavec) VALUES (%s, %s, %s)", (nombrec, correoc, clavecifrada))
        mysql.connection.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    brandplantsApp.secret_key = 'aaaaeeee'
    brandplantsApp.run(port = 3000,debug = True)

