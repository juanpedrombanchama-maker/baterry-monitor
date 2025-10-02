from flask import Flask, request, jsonify, render_template
import os
import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
estado_bateria = {"voltaje": 0.0, "porcentaje": 0.0}

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    if not data or "voltaje" not in data or "porcentaje" not in data:
        return jsonify({"status": "error", "message": "Datos incompletos"}), 400
    
    estado_bateria["voltaje"] = data.get("voltaje", 0.0)
    estado_bateria["porcentaje"] = data.get("porcentaje", 0.0)

    logging.info(f"Actualizado: {estado_bateria}")

    return jsonify({"status": "ok"})

@app.route('/nivel')
def nivel():
    return jsonify(estado_bateria)

@app.route('/')
def index():
    return render_template("index.html", voltaje=estado_bateria["voltaje"], porcentaje=estado_bateria["porcentaje"])


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
