from flask import Flask, render_template, request
from PIL import Image
from diffusers import DiffusionPipeline
import base64

app = Flask(__name__)

# Cargar el modelo de difusión
arte = DiffusionPipeline.from_pretrained(
    "lambdalabs/sd-image-variations-diffusers")

# Ruta inicial


@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar las imágenes seleccionadas


@app.route('/procesar', methods=['POST'])
def procesar_imagenes():
    if 'file' not in request.files:
        return 'No se seleccionó ninguna imagen.'

    # Obtener la imagen del formulario
    archivo = request.files['file']
    imagen = Image.open(archivo)

    # Procesar la imagen utilizando el modelo de difusión
    imagen_procesada = arte(imagen)

    # Convertir la imagen procesada a base64 para mostrarla en el navegador
    buffered = io.BytesIO()
    imagen_procesada.save(buffered, format="JPEG")
    imagen_codificada = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return render_template('resultado.html', imagen=imagen_codificada)


if __name__ == '__main__':
    app.run(debug=True)
