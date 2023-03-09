from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perguntas')
def perguntas():
    return render_template('perguntas.html')

@app.route('/teste')
def teste():
    return render_template('teste.html')

@app.route('/surpresa')
def surpresa():
    return render_template('surpresa.html')

@app.route('/senha')
def senha():
    return render_template('senha.html')

if __name__ == '__main__':
    app.run(debug=True)
