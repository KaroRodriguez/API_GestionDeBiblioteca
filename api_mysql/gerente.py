from flask import Flask, request, jsonify

app = Flask(__name__) #crear app

gerentes = [] #falsa bd

@app.route("/crear-gerente", methods=["POST"])  #crear url
def crear_gerente():
    data = request.get_json()
    if "gerente_id" not in data or not isinstance(data["gerente_id"], int):  #id entero valido
        return jsonify({"error": "Se requiere un gerente_id válido"}), 400   #error 400

    for gerente in gerentes:  #iteracion en la lista
        if gerente["gerente_id"] == data["gerente_id"]:
            return jsonify({"error": "El gerente_id ya existe"}), 400

    gerentes.append(data)   #nuevo gerente
    return jsonify(data), 201   #201 creado

@app.route("/buscar-gerente/<int:gerente_id>", methods=["GET"])   #traer
def buscar_gerente(gerente_id):
    for gerente in gerentes:
        if gerente["gerente_id"] == gerente_id:
            return jsonify(gerente), 200
    return jsonify({"error": "Gerente no encontrado"}), 404

@app.route("/borrar-gerente/<int:gerente_id>", methods=["DELETE"])    #borrar
def borrar_gerente(gerente_id):    
    global gerentes   #modificar lista
    gerente_a_eliminar = None   #var para eliminar
    for gerente in gerentes:     #iterar la lista
        if gerente["gerente_id"] == gerente_id:
            gerente_a_eliminar = gerente
            break

    if gerente_a_eliminar:
        gerentes.remove(gerente_a_eliminar)  #borra
        return jsonify({"message": f"Gerente con ID {gerente_id} eliminado"}), 200  #borrado
    else:
        return jsonify({"error": "Gerente no encontrado"}), 404  #error

@app.route("/gerentes", methods=["GET"])     #traer todos los gerentes
def obtener_gerentes():
    return jsonify(gerentes), 200

if __name__ == "__main__":
    app.run(debug=True)