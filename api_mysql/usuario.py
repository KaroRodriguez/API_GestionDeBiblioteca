from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route("/crear-usuario", methods=["POST"])
def crear_usuario():
    data = request.get_json()
    if "user_id" not in data or not isinstance(data["user_id"], int):
        return jsonify({"error": "Se requiere un user_id válido"}), 400

    for usuario in usuarios:
        if usuario["user_id"] == data["user_id"]:
            return jsonify({"error": "El user_id ya existe"}), 400

    usuarios.append(data)
    return jsonify(data), 201

@app.route("/buscar-usuario/<int:user_id>", methods=["GET"])
def buscar_usuario(user_id):
    for usuario in usuarios:
        if usuario["user_id"] == user_id:
            return jsonify(usuario), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

@app.route("/borrar-usuario/<int:user_id>", methods=["DELETE"])
def borrar_usuario(user_id):
    global usuarios
    usuario_a_eliminar = None
    for usuario in usuarios:
        if usuario["user_id"] == user_id:
            usuario_a_eliminar = usuario
            break

    if usuario_a_eliminar:
        usuarios.remove(usuario_a_eliminar)
        return jsonify({"message": f"Usuario con ID {user_id} eliminado"}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify(usuarios), 200

if __name__ == "__main__":
    app.run(debug=True)
