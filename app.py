from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Calculator API"

@app.route('/calc', methods=['GET'])
def calculate():
    result = None
    error = None

    a = request.args.get('a')
    b = request.args.get('b')
    op = request.args.get('op')

    if a and b and op:
        try:
            a = float(a)
            b = float(b)

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
        except ValueError:
            error = "Invalid input"

    return render_template('calc.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
