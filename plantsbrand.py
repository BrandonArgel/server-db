from flask import Flask, render_template
brandplantsApp = Flask(__name__)
@brandplantsApp.route('/')
def index():
    return render_template('inicio.html')
    
@brandplantsApp.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    brandplantsApp.secret_key = 'aaaaeeee'
    brandplantsApp.run(port = 3000,debug = True)

