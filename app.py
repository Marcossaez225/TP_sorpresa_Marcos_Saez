from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Página de inicio'

@app.route('/contacto')
def contacto():
    return 'Página de contacto'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
