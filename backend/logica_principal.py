import requests
import os
import shutil
from PyQt5.QtCore import QObject, pyqtSignal

class LogicaPrincipal(QObject):
    '''
    Clase destinada a realizar las tareas de lógica detrás de la aplicación, como comunicarse con
    la API y manejar los archivos
    '''

    senal_mostrar_menu = pyqtSignal()
    senal_enviar_jpg = pyqtSignal(str, str)
    senal_enviar_gif = pyqtSignal(str, str)

    def __init__(self) -> None:
        super().__init__()
        self.tipo = ''
        self.categoria = ''
    
    def iniciar_menu(self, tipo : str, categoria : str):
        '''
        Es llamado cada vez que el menú principal pasa de estar oculto a visible. Obtiene la
        primera imagen y avisa al frontend para que la muestre, junto a la ventana
        '''
        self.tipo = tipo
        self.categoria = categoria
        nueva_imagen, extension, nombre = self.obtener_imagen()
        self.actualizar_menu(nueva_imagen, extension, nombre)
        self.senal_mostrar_menu.emit()

    def siguiente_imagen(self):
        nueva_imagen, extension, nombre = self.obtener_imagen()
        self.actualizar_menu(nueva_imagen, extension, nombre)
    
    def obtener_imagen(self):
        '''
        Realiza la request HTTP a la API para obtener el link a una imagen. Después obtiene el
        contenido en bytes de esa imagen y la guarda en un nuevo archivo temporal. Retorna una
        tupla donde el primer valor es la ruta de la imagen, y el segundo valor es el tipo
        ('gif' o 'jpg')
        '''
        respuesta = requests.get(f'https://api.waifu.pics/{self.tipo}/{self.categoria}')
        url_imagen = respuesta.json()['url']
        imagen = requests.get(url_imagen)
        self.imagen = imagen
        if imagen.headers['content-type'] == 'image/gif':
            extension = 'gif'
        else:
            extension = 'jpg'
        ruta_archivo = os.path.join('images', f'actual.{extension}')
        with open (ruta_archivo, 'wb') as f:
            f.write(imagen.content)
        nombre = url_imagen.split('/')[-1]
        return (ruta_archivo, extension, nombre)
    
    def actualizar_menu(self, nueva_imagen : str, extension : str, nombre : str):
        if extension == 'gif':
            self.senal_enviar_gif.emit(nueva_imagen, nombre)
        elif extension == 'jpg':
            self.senal_enviar_jpg.emit(nueva_imagen, nombre)
    
    def guardar_imagen(self, directorio, nombre):
        ruta_archivo = os.path.join(directorio, nombre)
        with open(ruta_archivo, 'wb') as f:
            f.write(self.imagen.content)
    
    def resetear_atributos(self):
        self.tipo = ''
        self.categoria = ''

if __name__ == '__main__':
    ruta1 = 'C:/Users/vmdia/Desktop/Proyectos/API/Anime-images-generator/images'
    ruta2 = 'imagen.jpg'
    ruta = os.path.join(ruta1, ruta2)
    print(ruta)