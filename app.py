from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

#Para cargar los productos

def cargar_productos():
    if os.path.exists("productos.json"):
       with open("productos.json" , "r") as archivo:
          return json.load(archivo)
    else:
       return []

# Para guardar los productos

def guardar_productos(productos):
    with open("productos.json", "w") as archivo:
        json.dump(productos, archivo, indent=4)

@app.route("/")
def index():
    productos = cargar_productos()
    return render_template("index.html", productos=productos)

@app.route("/carrito")
def carrito():
    return render_template("carrito.html")

@app.route("/admin")
def admin():
    productos = cargar_productos()
    return render_template("admin.html", productos=productos)

@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = request.form["precio"]

        productos = cargar_productos()

        productos.append({
            "nombre": nombre,
            "precio": precio
        })

        guardar_productos(productos)

        return redirect(url_for("admin"))

    return render_template("agregar.html")

if __name__ == "__main__":
    app.run(debug=True)