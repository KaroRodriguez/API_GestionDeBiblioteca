from flask import Flask, request, jsonify

app = Flask(__name__)

libros = [] #falsa bd

@app.route("/crear-libro", methods=["POST"])  #crear
def crear_libro():
    data = request.get_json()
    if "libro_id" not in data or not isinstance(data["libro_id"], int):
        return jsonify({"error": "Se requiere un libro_id válido"}), 400

    for libro in libros:
        if libro["libro_id"] == data["libro_id"]:
            return jsonify({"error": "El libro_id ya existe"}), 400

    libros.append(data)
    return jsonify(data), 201

@app.route("/buscar-libro/<int:libro_id>", methods=["GET"])
def buscar_libro(libro_id):
    for libro in libros:
        if libro["libro_id"] == libro_id:
            return jsonify(libro), 200
    return jsonify({"error": "Libro no encontrado"}), 404

@app.route("/borrar-libro/<int:libro_id>", methods=["DELETE"])
def borrar_libro(libro_id):
    global libros
    libro_a_eliminar = None
    for libro in libros:
        if libro["libro_id"] == libro_id:
            libro_a_eliminar = libro
            break

    if libro_a_eliminar:
        libro.remove(libro_a_eliminar)
        return jsonify({"message": f"Libro con ID {libro_id} eliminado"}), 200
    else:
        return jsonify({"error": "Libro no encontrado"}), 404

@app.route("/libros", methods=["GET"])
def obtener_libros():
    return jsonify(libros), 200

@app.route("/actualizar-libro/<int:libro_id>", methods=["PUT"])
def actualizar_libro(libro_id):
    data = request.get_json()
    for i, libro in enumerate(libros):
        if libro["libro_id"] == libro_id:
            libro[i] = data
            return jsonify(data), 200
        return jsonify({"error": "Libro no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)