from flask import Flask, request, jsonify

app = Flask(__name__)
estado_bateria = {"voltaje": 0.0, "porcentaje": 0.0}

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    estado_bateria["voltaje"] = data.get("voltaje", 0.0)
    estado_bateria["porcentaje"] = data.get("porcentaje", 0.0)
    return jsonify({"status": "ok"})

@app.route('/nivel')
def nivel():
    return jsonify(estado_bateria)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

