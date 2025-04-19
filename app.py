from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Calculator API"

@app.route('/calc', methods=['GET'])
def calculate():
    result = None
    error = None
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
                error = "Division by zero is not allowed"
        else:
            error = "Invalid operation"
    except:
        if request.args:
            error = "Invalid input"

    return render_template('calc.html', result=result, error=error)
