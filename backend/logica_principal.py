import requests
import os
from PyQt5.QtCore import QObject, pyqtSignal
from requests.api import request

class LogicaPrincipal(QObject):
    '''
    Clase destinada a realizar las tareas de lógica detrás de la aplicación, como comunicarse con
    la API y manejar los archivos
    '''

    senal_mostrar_menu = pyqtSignal()

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
        nueva_imagen = self.obtener_imagen()
        self.actualizar_menu(nueva_imagen)
        self.senal_mostrar_menu.emit()

    def obtener_imagen(self):
        '''
        Realiza la request HTTP a la API para obtener el link a una imagen. Después obtiene el
        contenido en bytes de esa imagen y la guarda en un nuevo archivo temporal
        '''
        respuesta = requests.get(f'https://api.waifu.pics/{self.tipo}/{self.categoria}')
        url_imagen = respuesta.json()['url']
        imagen = requests.get(url_imagen)
        if imagen.headers['content-type'] == 'image/gif':
            extension = 'gif'
        else:
            extension = 'jpg'
        ruta_archivo = os.path.join('images', f'actual.{extension}')
        with open (ruta_archivo, 'wb') as f:
            f.write(imagen.content)
        return ruta_archivo
        

    def actualizar_menu(self, nueva_imagen : str):
        pass