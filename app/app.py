from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "¡Hola desde Flask en Vercel!"})  # Cambia el mensaje para confirmar que es la versión nueva

# Elimina estas líneas (Vercel maneja el host/port automáticamente):
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)