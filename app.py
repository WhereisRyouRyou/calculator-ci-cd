from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Calculator API"

@app.route('/calc', methods=['GET'])
def calculate():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        op = request.args.get('op')

        if op == 'add':
            result = a + b
        elif op == 'sub':
            result = a - b
        elif op == 'mul':
            result = a * b
        elif op == 'div':
            if b != 0:
                result = a / b
            else:
                return jsonify({"error": "Division by zero is not allowed"}), 400
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result})

    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True)
