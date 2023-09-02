from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome All'

@app.route('/addition', methods=["Get"])
def addition():
    a = request.args.get("num1")
    b = request.args.get("num2")
    print(f"Received num1={a}, num2={b}")
    result = int(a) + int(b)
    print(f"Result: {result}")
    return str(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
