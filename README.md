# GeoportalCX
## Geoportal para el procesamiento de imagenes satelitales y monitoreo de inundaciones en diferentes regiones de Bolivia

[![N|Sekker](https://cldup.com/dTxpPi9lDf.thumb.png)](https://flask.palletsprojects.com/en/2.0.x/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Geoportal basico basado en el estado prurinacional de bolivia

## Documentacion sobre el proyecto


## Tabla de contenidos:

- [Introduccion](#Introduccion)
- [Descripción y contexto](#descripción-y-contexto)
- [Guía de usuario](#Geoportal(Desarrollo))
- [Guía de instalación](#guía-de-instalación)
- [Cómo utilizar Qgis](#Qgis)
- [Código](#código)
- [Autor/es](#autores)
- [Información adicional](#información-adicional)
- [Licencia](#licencia)
- [Limitación de responsabilidades - Solo BID](#limitación-de-responsabilidades)

## Introduccion
---
El presente proyecto, fundamentalmente tiene como objetivo brindar una visión en lo que respecta los cambios meteorológicos (inundaciones) y monitorización de las imágenes satelitales es importante realizar un análisis, plan regional y para esto se ha realizado una gran cantidad de investigaciones a nivel mundial sobre la evaluación del cambio del uso del suelo ya que es una parte fundamental para resaltar en el proyecto. Los cuales desde el primer lanzamiento de un satélite en este caso el “Earth Resources Technology Satellite” en 1972 (renombrado Landsat 1), ha logrado un gran desarrollo en los proyectos de análisis que están vinculados con mapeo y monitoreo del medio ambiente (Fragoso, 2017). 

## Descripción y contexto
---
**Inundaciones**
Según Vargas & Vihar (2017) explican que es un estado en el que el nivel del agua de un río u océano es alto, lo que provoca la inundación de tierras que normalmente no están sumergidas, lo que también es un fenómeno natural que no se puede diagnosticar una vez que se produce. Las inundaciones pueden ocurrir en cualquier momento, pueden llevar horas o incluso ocurrir accidentalmente sin previo aviso.
Todos los países se enfrentan a inundaciones, ya sea debido a las altas precipitaciones, el desbordamiento de los ríos, mal flujo de agua o simplemente debido a una combinación de factores.

**Imágenes satelitales**
Las imágenes satelitales también conocidas como imágenes de observación de la Tierra, fotografías desde el espacio o simplemente fotografías de satélite son el producto obtenido por un sensor instalado a bordo de un satélite artificial, mediante la captación de la radiación electromagnética emitida o reflejada por un cuerpo, que posteriormente se transmite a estaciones terrenas para su visualización, procesamiento y análisis.

**Teledetección**
Es una tecnología que adquiere datos de la superficie de la tierra a través de sensores instalados en plataformas espaciales. La interacción electromagnética entre el suelo y el sensor produce una serie de datos que se pueden procesar para obtener información interpretable de la Tierra (Instituto Geográfico Nacional, 2018).




## Geoportal(Desarrollo)
---
El Desarrollo fue realizado con el lenguaje Python y con el Framework Flask, se optó por estas herramientas ya que se acomodan de acuerdo al tamaño y tipo proyecto que se tiene. El proyecto fue pensado en primera instancia para funcionar de manera local
todos los datos cargados al GeoPortal son almacenados dentro una Base de Datos la cual es Mysql. 

 	
## Guía de instalación
Requiere  [python ](https://www.python.org/downloads/) v6.3+.
Instalacion de la dependencia flask npm
 sh
pip install Flask



## Qgis 
---
QGIS es un Sistema de Información Geográfica (SIG) de Código Abierto licenciado bajo GNU - General Public License . QGIS es un proyecto oficial de Open Source Geospatial Foundation (OSGeo).

Principales herramientas que QGIS nos proporciona en el campo de la teledetección
Cálculo de estadísticas e histogramas.
Filtrajes.
Corrección de imágenes de satélite.
Clasificación de imágenes de satélite.
Detección de cambios.
Cálculo de índices de vegetación y monitorización de incendios.

## código
---
**INDEX**
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

    
**Controller**
from bd import obtener_conexion
from index import image

def inser(titulo, ciudad, image, descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO image(titulo, ciudad, image, descripcion) VALUES (%s, %s, %s, %s)",
                       (titulo, ciudad, image, descripcion))
    conexion.commit()
    conexion.close()


def views():
    conexion = obtener_conexion()
    image = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, titulo, ciudad, image, descripcion FROM image")
        image = cursor.fetchall()
    conexion.close()
    return image

def viewPanel(id):
    conexion = obtener_conexion()
    image = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, titulo, ciudad, image, descripcion FROM image WHERE id = %s", (id,))
        image = cursor.fetchone()
    conexion.close()
    return image
   
## Autor/es
---
**ALEX JAVIER CHURA CUSI** (https://cldup.com/dTxpPi9lDf.thumb.png)](https://flask.palletsprojects.com/en/2.0.x/)

**RICHARD CALLISAYA PUSARICO**

**EDDY GONZALO ARGUEDAS MOYA**

**JORGE GALVEZ CLAROS**

**ABRAHAM QUIROGA GUZMAN**


## Información adicional
---


## Licencia

open Source

**Free Software!**
