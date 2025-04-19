from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML for the form
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
</head>
<body>
    <h1>Simple Calculator</h1>
    <form method="get" action="/calc">
        <input type="number" step="any" name="a" placeholder="First number" required>
        <select name="op">
            <option value="add">+</option>
            <option value="sub">−</option>
            <option value="mul">×</option>
            <option value="div">÷</option>
        </select>
        <input type="number" step="any" name="b" placeholder="Second number" required>
        <button type="submit">Calculate</button>
    </form>
    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% elif error %}
        <h2 style="color:red;">Error: {{ error }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_form, result=None, error=None)

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
                return render_template_string(html_form, result=None, error="Division by zero is not allowed")
        else:
            return render_template_string(html_form, result=None, error="Invalid operation")

        return render_template_string(html_form, result=result, error=None)

    except ValueError:
        return render_template_string(html_form, result=None, error="Invalid input")

if __name__ == '__main__':
    app.run(debug=True)

