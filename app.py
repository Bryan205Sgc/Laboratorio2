from flask import Flask, render_template, request, jsonify
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('Login.html')

@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    return render_template('registrarse.html')

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html')


@app.route('/procesar_datos', methods=['POST'])
def procesar_datos():
    if request.method == 'POST':
        username = request.form.get('username')
        rol = request.form.get('rol')
        permisos = [
            '1' if request.form.get('permisos_agregar') == 'on' else '0',
            '1' if request.form.get('permisos_eliminar') == 'on' else '0',
            '1' if request.form.get('permisos_visualizar') == 'on' else '0',
            '1' if request.form.get('permisos_editar') == 'on' else '0'
        ]

        #El json es solo para comprobar que si esté mandando los datos XD lo podes quitar si querés
        return jsonify({
            "username": username,
            "rol": rol,
            "permisos": permisos
        })

    return render_template('menu.html')


if __name__ == '__main__':
    app.run(debug=True)