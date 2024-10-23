from flask import Flask, jsonify

app = Flask(__name__)

# Datos hardcodeados
datos = [
    {"id": 1, "nombre": "Elemento 1", "descripcion": "Descripción del elemento 1"},
    {"id": 2, "nombre": "Elemento 2", "descripcion": "Descripción del elemento 2"},
]

@app.route('/api/datos', methods=['GET'])
def obtener_datos():
    return jsonify(datos), 200

if __name__ == '__main__':
    app.run(debug=True)
