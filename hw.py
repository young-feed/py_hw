from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # host='0.0.0.0' позволяет принимать запросы со всех интерфейсов
    # port=5000 — стандартный порт для Flask
    app.run(host='0.0.0.0', port=5000)
