from flask import Flask, render_template, request, url_for, redirect, flash
from flask.globals import session
from flask.helpers import flash
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
    
@brandplantsApp.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        correoc = request.form['correo']
        clavec = request.form['clave'].encode('utf-8')
        selcliente = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        selcliente.execute("SELECT * FROM cliente WHERE correoc = %s", (correoc,))
        c = selcliente.fetchone()
        selcliente.close()
        if c is not None:
            if bcrypt.hashpw(clavec, c['clavec'].encode('utf-8')) == c['clavec'].encode('utf-8'):
                session['nombrec'] = c['nombrec']
                session['correoc'] = c['correoc']
                return render_template('cliente.html')
            else:
                flash('Contraseña incorrecta')
                return redirect(request.url)
        else:
            correou = request.form['correo']
            claveu = request.form['clave'].encode('utf-8')
            selusuario = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            selusuario.execute("SELECT * FROM usuario WHERE correou = %s", (correou,))
            u = selusuario.fetchone()
            if u is not None:
                if bcrypt.hashpw(claveu, u['claveu'].encode('utf-8')) == u['claveu'].encode('utf-8'):
                    session['nombreu'] = u['nombreu']
                    session['correou'] = u['correou']
                    return render_template('usuario.html')
                else:
                    flash('Contraseña incorrecta')
                    return redirect(request.url)
            else:
                flash('Usuario inexistente')
                return redirect(request.url)
    else:       
        return render_template('login.html')

@brandplantsApp.route('/logout', methods = ['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))

@brandplantsApp.route('/cliente', methods = ['GET', 'POST'])
def cliente():
    return render_template('cliente.html')

@brandplantsApp.route('/usuario', methods = ['GET', 'POST'])
def usuario():
    return render_template('usuario.html')

@brandplantsApp.route('/tienda', methods = ['GET', 'POST'])
def tienda():
    selproducto = mysql.connection.cursor()
    selproducto.execute("SELECT * FROM producto")
    p = selproducto.fetchall()
    return render_template('tienda.html', productos = p)


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

@brandplantsApp.route('/sCliente', methods =['GET', 'POST'])
def sCliente():
    selCliente = mysql.connection.cursor()
    selCliente.execute("SELECT * FROM cliente")
    c = selCliente.fetchall()
    return render_template('ucliente.html', clientes = c)
    
@brandplantsApp.route('/uCliente', methods =['GET', 'POST'])
def uCliente():
    idcliente = request.form['idcliente']
    if request.method == 'POST':
        nombrec = request.form['nombrec']
        correoc = request.form['correoc']
        clavec = request.form['clavec'].encode('utf-8')
        clavecifrada = bcrypt.hashpw(clavec, bcrypt.gensalt())
        actcliente = mysql.connection.cursor()
        actcliente.execute("UPDATE cliente SET nombrec=%s,correoc=%s,clavec=%s WHERE idcliente=%s", (nombrec,correoc, clavecifrada, idcliente))
        mysql.connection.commit()
        flash('Se ha actualizado el registro correctamente')
        return redirect(url_for('sCliente'))

@brandplantsApp.route('/dCliente', methods =['GET', 'POST'])
def dCliente():
    idcliente = request.form['idcliente']
    delcliente = mysql.connection.cursor()
    delcliente.execute("DELETE FROM cliente WHERE idcliente=%s", (idcliente,))
    mysql.connection.commit()
    flash('Se ha eliminado el registro correctamente')
    return redirect(url_for('sCliente'))

@brandplantsApp.route('/iCliente', methods = ['GET', 'POST'])
def iCliente():
    if request.method == 'POST':
        nombrec = request.form['nombrec']
        correoc = request.form['correoc']
        clavec = request.form['clavec'].encode('utf-8')
        clavecifrada = bcrypt.hashpw(clavec, bcrypt.gensalt())
        regcliente = mysql.connection.cursor()
        regcliente.execute("INSERT INTO cliente (nombrec, correoc, clavec) VALUES (%s, %s, %s)", (nombrec, correoc, clavecifrada))
        mysql.connection.commit()
        flash('Cliente agregado')
    return redirect(url_for('sCliente'))

# Productos
@brandplantsApp.route('/sProducto', methods = ['GET', 'POST'])
def productos():
    selproducto = mysql.connection.cursor()
    selproducto.execute("SELECT * FROM producto")
    p = selproducto.fetchall()
    return render_template('productos.html', productos = p)

@brandplantsApp.route('/uProducto', methods =['GET', 'POST'])
def uProducto():
    idproducto = request.form['idproducto']
    if request.method == 'POST':
        nombrep = request.form['nombrep']
        tipop = request.form['tipop']
        imagenp = request.form['imagenp']
        descripcionp = request.form['descripcionp']
        preciop = request.form['preciop']
        actproducto = mysql.connection.cursor()
        actproducto.execute("UPDATE producto SET nombrep=%s,tipop=%s,imagenp=%s,descripcionp=%s,preciop=%s WHERE idproducto=%s", (nombrep, tipop, imagenp,descripcionp,preciop, idproducto))
        mysql.connection.commit()
        flash('Se ha actualizado el registro correctamente')
        return redirect(url_for('productos'))

@brandplantsApp.route('/dProducto', methods =['GET', 'POST'])
def dProducto():
    idproducto = request.form['idproducto']
    delproducto = mysql.connection.cursor()
    delproducto.execute("DELETE FROM producto WHERE idproducto=%s", (idproducto,))
    mysql.connection.commit()
    flash('Se ha eliminado el producto correctamente')
    return redirect(url_for('productos'))

@brandplantsApp.route('/iProducto', methods = ['GET', 'POST'])
def iProducto():
    if request.method == 'POST':
        nombrep = request.form['nombrep']
        tipop = request.form['tipop']
        imagenp = request.form['imagenp']
        descripcionp = request.form['descripcionp']
        preciop = request.form['preciop']
        actproducto = mysql.connection.cursor()
        actproducto.execute("INSERT INTO producto (nombrep, tipop, imagenp, descripcionp, preciop) VALUES(%s, %s, %s, %s, %s)", (nombrep, tipop, imagenp, descripcionp, preciop))
        mysql.connection.commit()
        flash('Se ha agregado el producto correctamente')
        return redirect(url_for('productos'))

if __name__ == '__main__':
    brandplantsApp.secret_key = 'aaaaeeee'
    brandplantsApp.run(port = 3000, debug = True)

