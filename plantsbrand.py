from flask import Flask, render_template, request, url_for
# from flask_mysqldb import MySQL, MySQLdb
# from flask_bcrypt import bcrypt 
brandplantsApp = Flask(__name__)
brandplantsApp.config['MYSQL_HOST'] = 'localhost'
brandplantsApp.config['MYSQL_USER'] = 'root'
brandplantsApp.config['MYSQL_PASSWORD'] = 'mysql'
brandplantsApp.config['MYSQL_DB'] = 'brandplants.sql'
brandplantsApp.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# mysql = MySQL(brandplantsApp)
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
        claveCifrada = bcrypt.hashpw(clavec, bcrypt.gensalt())
        regCliente = mysql.connection.cursor()
        regCliente.execute("INSERT INTO cliente (nombrec, correoc, clavec) VALUES (%s, %s, %s)", (nombrec, correoc, claveCifrada))
        mysql.connection.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    brandplantsApp.secret_key = 'aaaaeeee'
    brandplantsApp.run(port = 3000,debug = True)

