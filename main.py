from flask import Flask, request, jsonify
from app import calculator

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Calculator API is running!"})

@app.route('/calc', methods=['GET'])
def calculate():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    op = request.args.get("op")

    try:
        if op == "add":
            result = calculator.add(a, b)
        elif op == "sub":
            result = calculator.subtract(a, b)
        elif op == "mul":
            result = calculator.multiply(a, b)
        elif op == "div":
            result = calculator.divide(a, b)
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
