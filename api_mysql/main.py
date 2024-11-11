from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/get-user/<user_id>")  #Este decorador define una ruta para la URL
def get_user(user_id):    #es un parámetro de la ruta que se pasará a la función get_user
    user_data = {
        "user_id": user_id,
        "name": "Jonh Doe",
        "email": "jondoe@gnail.com"
    }
    extra = request.args.get("extra")     #Obtiene el parámetro extra de la cadena de consulta de la URL (si está presente).
    if extra:                             #Si el parámetro extra está presente, se añade al diccionario user_data.
        user_data["extra"] = extra

        return jsonify(user_data), 200         #Devuelve el diccionario user_data en formato JSON junto con un código de estado HTTP 200 (OK)
    
@app.route("/create-user", methods=["POST"])      
def create_user():
    data = request.get_json()
                              
    return jsonify(data), 201                    #Devuelve los datos recibidos en formato JSON junto con un código de estado HTTP 201 (Created).



if __name__ == "__main__":
    app.run(debug=True)