import requests
from PyQt5.QtCore import QObject, pyqtSignal

class LogicaPrincipal(QObject):
    '''
    Clase destinada a realizar las tareas de lógica detrás de la aplicación, como comunicarse con
    la API y manejar los archivos
    '''

    senal_mostrar_menu = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
    
    def iniciar_menu(self, tipo : str, categoria : str):
        self.senal_mostrar_menu.emit()

    def obtener_imagen(self, tipo : str, categoria : str):
        pass

    def actualizar_menu(self, nueva_imagen : str):
        pass