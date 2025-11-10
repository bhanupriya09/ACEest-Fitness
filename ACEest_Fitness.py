from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="healthy")

@app.route("/classes")
def classes():
    return jsonify(
        classes=["Yoga", "HIIT", "Spin", "Zumba", "CrossFit"]
    )

@app.route("/membership")
def membership():
    return jsonify(
        plans=[
            {"type": "Basic", "price": 30},
            {"type": "Premium", "price": 50},
            {"type": "Elite", "price": 80}
        ]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
