from flask import Flask, render_template, request, jsonify, redirect, url_for
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

@app.route('/productos', methods=['GET','POST'])
def productos():
    return render_template('productos.html')


@app.route('/productos')
def ver_productos():
    return render_template('productos.html', productos=productos)

# Ruta para agregar un nuevo producto (GET muestra el formulario, POST guarda el producto)
@app.route('/productos/agregar', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nuevo_producto = {
            "idproducto": len(productos) + 1,  # ID automático basado en la cantidad de productos
            "producto": request.form['producto'],
            "precio": float(request.form['precio'])
        }
        productos.append(nuevo_producto)
        return redirect(url_for('ver_productos'))
    return render_template('productos_agregar.html')

# Ruta para modificar un producto existente (GET muestra el formulario, POST guarda los cambios)
@app.route('/productos/modificar/<int:id>', methods=['GET', 'POST'])
def modificar_producto(id):
    producto = next((p for p in productos if p["idproducto"] == id), None)
    if not producto:
        return "Producto no encontrado", 404

    if request.method == 'POST':
        producto['producto'] = request.form['producto']
        producto['precio'] = float(request.form['precio'])
        return redirect(url_for('ver_productos'))

    return render_template('productos_modificar.html', producto=producto)

# Ruta para eliminar un producto
@app.route('/productos/eliminar/<int:id>')
def eliminar_producto(id):
    global productos
    productos = [p for p in productos if p["idproducto"] != id]
    return redirect(url_for('ver_productos'))

# Ruta para ver un solo producto (opcional)
@app.route('/productos/<int:id>')
def ver_producto(id):
    producto = next((p for p in productos if p["idproducto"] == id), None)
    if not producto:
        return "Producto no encontrado", 404
    return jsonify(producto)


if __name__ == '__main__':
    app.run(debug=True)