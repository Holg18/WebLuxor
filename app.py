from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/models')
def models():
    # En una aplicación real, aquí cargarías datos de una base de datos
    models_data = [
    {
        'name': 'ALANA PEARCE',
        'category': 'Women',
        'image': 'https://luxoragenciamodels.com/wp-content/uploads/2022/12/modelo_3.png'
    },

    {
        'name': 'ANNEDUBOIS',
        'category': 'Women',
        'image': 'https://luxoragenciamodels.com/wp-content/uploads/2022/12/modelo_1.png'
    },
       {
        'name': 'NICOLE WESLEY',
        'category': 'Women',
        'image': 'https://luxoragenciamodels.com/wp-content/uploads/2022/12/modelo.png'
    },

    {
        'name': 'Jacob_rodriguez',
        'category': 'men',
        'image': 'https://i.ibb.co/XkxyxcYJ/perfil-about-me.png'
    },
    {
        'name': 'Ruso_Miers',
        'category': 'men',
        'image': 'https://images.squarespace-cdn.com/content/v1/5b46e884aa49a10f1fffa15a/1537381021418-EPGME124R3S0VSHW10MY/port.jpg'
    },
    {
        'name': 'Zack_Miller',
        'category': 'new-faces',
        'image': 'https://static.vecteezy.com/system/resources/thumbnails/003/492/236/small/portrait-of-brutal-handsome-bearded-young-man-model-in-white-shirt-standing-and-looking-at-the-camera-with-pleasure-proud-face-indoor-studio-shot-isolated-on-beige-background-free-photo.JPG'
    },
    {
        'name': 'Thiago_Dasilva',
        'category': 'new-faces',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/David_Gandy_SS17.jpg/1200px-David_Gandy_SS17.jpg'
    },
    
    
]
    
    return render_template('models.html', models=models_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)