from flask import Flask, request

app = Flask(__name__) #everything will become a main file now

pickle_in = open('model.pkl', 'rb')

@app.route('/') #decorator
def add():
    a = request.args.get('num1') # num1 = 10 provided in the browser only
    b = request.args.get('num2') # num2 = 20 provided in the browser only
    return ([int(a) + int(b)])


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port= 8000) 