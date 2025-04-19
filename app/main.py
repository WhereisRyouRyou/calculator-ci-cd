from flask import Flask, request, jsonify
from calculator import calculate

app = Flask(__name__)

@app.route('/calc')
def calc():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        op = request.args.get('op')
        result = calculate(a, b, op)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
