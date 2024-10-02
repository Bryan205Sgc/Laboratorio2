from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('Login.html')

@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    return render_template('registrarse.html')

if __name__ == '__main__':
    app.run(debug=True)