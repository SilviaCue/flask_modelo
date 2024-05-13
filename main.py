import io
import os
import torch
from diffusers import DiffusionPipeline
from PIL import Image
from flask import Flask, render_template, request
import base64

app = Flask(__name__)

# Cargar el modelo de difusión
arte = DiffusionPipeline.from_pretrained(
    "lambdalabs/sd-image-variations-diffusers")

# Definir la ruta para la página principal


@app.route('/')
def index():
    return render_template('index.html')

# Definir la ruta para procesar las imágenes


@app.route('/procesar', methods=['POST'])
def procesar_imagenes():
    # Obtener las imágenes del formulario
    archivos = request.files.getlist('file')

    # Procesar cada imagen individualmente
    imagenes_procesadas = []
    for archivo in archivos:
        imagen = Image.open(archivo)

        # Procesar la imagen utilizando el modelo de difusión
        imagen_procesada = arte(imagen)

        # Convertir la imagen procesada a base64
        buffered = io.BytesIO()
        imagen_procesada.save(buffered, format="JPEG")
        imagen_codificada = base64.b64encode(
            buffered.getvalue()).decode("utf-8")
        imagenes_procesadas.append(imagen_codificada)

    return render_template('index.html', imagenes=imagenes_procesadas)


if __name__ == '__main__':
    app.run(debug=True)
