from flask import Flask
# app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Vedant Patel 1.7'

if __name__ == '__main__':
    app.run()
