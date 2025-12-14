from flask import Flask, request, jsonify, render_template
import os
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

estado_baterias = {}

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    if not data or "id" not in data or "voltaje" not in data or "porcentaje" not in data:
        return jsonify({"status": "error", "message": "Datos incompletos"}), 400

    id_bateria = data["id"]
    try:
        voltaje = float(data["voltaje"])
        porcentaje = float(data["porcentaje"])
        if not (0 <= porcentaje <= 100):
            raise ValueError("Porcentaje fuera de rango")
    except (ValueError, TypeError):
        return jsonify({"status": "error", "message": "Datos inválidos"}), 400

    estado_baterias[id_bateria] = {
        "voltaje": voltaje,
        "porcentaje": porcentaje
    }

    logging.info(f"Actualizado {id_bateria}: {estado_baterias[id_bateria]}")
    return jsonify({"status": "ok"})

@app.route('/nivel')
def nivel():
    return jsonify(estado_baterias)

@app.route('/')
def index():
    return render_template("index.html", baterias=estado_baterias)

@app.route('/Ayuda')
def Ayuda():
    return render_template("Ayuda.html")

@app.route('/Sugerncias')
def Sugerencias():
    return render_template("Sugerencias.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
