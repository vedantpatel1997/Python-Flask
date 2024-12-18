from flask import Flask

app = Flask(__name__)  # Uncommented to define the app object

@app.route('/')
def hello_world():
    return 'Hello, Vedant Patel 1.8'

if __name__ == '__main__':
    app.run()
