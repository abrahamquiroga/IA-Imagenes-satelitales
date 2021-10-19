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

