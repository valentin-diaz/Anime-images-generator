from PyQt5.QtCore import QLine, pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QFont, QPixelFormat, QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget)
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout)
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, QAction)

import parametros as p

class MenuSeleccion(QWidget):
    '''
    Permite elegir el tipo de imágenes que se van a recibir (SFW o NSFW) y la categoría. Además, debe decir de alguna forma la diferencia entre los dos tipos, y en caso de elegir NSFW, muestra una advertencia y pide confirmar la elección
    '''

    def __init__(self) -> None:
        super().__init__()
        self.init_gui()
    
    def init_gui(self):
        # Configuración inicial de la ventana
        self.setGeometry(*p.GEOMETRY_ARGS)
        self.setWindowTitle(p.TITULO)
        self.setStyleSheet(f'background-color : {p.COLOR_FONDO};')