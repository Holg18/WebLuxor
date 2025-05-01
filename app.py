from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/models')
def models():
    # Obtener el parámetro de categoría de la URL (por defecto 'todos')
    categoria = request.args.get('categoria', 'todos')
    return render_template('models.html', categoria=categoria)

@app.route('/novedades')
def novedades():
    return render_template('novedades.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)