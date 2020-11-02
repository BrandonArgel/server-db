from flask import Flask, render_template
brandplantsApp = Flask(__name__)
@brandplantsApp.route('/')
def index():
    return render_template('inicio.html')
    
if __name__ == '__main__':
    brandplantsApp.secret_key = 'aaaaeeee'
    brandplantsApp.run(port = 3000,debug = True)