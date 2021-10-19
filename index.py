from logging import debug
import os
import cv2
from flask import Flask, app, render_template, request, redirect, flash, url_for, send_from_directory
from werkzeug.utils import secure_filename
import controller

UPLOAD_FOLDER = './static/image'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    image = controller.views()
    return render_template('content.html', image = image)

@app.route('/contact')
def contact():
    image = controller.views()
    return render_template('contact.html', image = image)

@app.route('/image')
def image():
    image = controller.views()
    return render_template('image.html', image = image)

@app.route('/addimage', methods=["POST", "GET"])
def addimage():
    return render_template('add.html')

@app.route('/add', methods=["POST", "GET"])
def add():
    titulo = request.form["titulo"]
    ciudad = request.form["ciudad"]
    descripcion = request.form["descripcion"]
    file = request.files["image"]
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    image = filename
    controller.inser(titulo, ciudad, image, descripcion)
    return redirect('/image')

@app.route('/viewPanel/<int:id>', methods=["POST", "GET"])
def viewPanel(id):
    image = controller.viewPanel(id)
    return render_template('vieww.html', image = image)

if __name__ == '__main__':
# Borar el debug = true al terminar la aplicacion    
    app.run()