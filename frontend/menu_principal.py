from PyQt5.QtCore import QLine, pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QFont, QPixelFormat, QPixmap
from PyQt5.QtWidgets import (QApplication, QComboBox, QMainWindow, QWidget)
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout)
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, QAction)

import parametros as p

class MenuPrincipal(QWidget):
    '''
    Muestra la imagen recibida, y permite al usuario elegir entre guardarla o descartarla
    '''

    def __init__(self) -> None:
        super().__init__()
        self.init_gui()
    
    def init_gui(self):
        # Configuración inicial de la ventana
        self.setGeometry(*p.GEOMETRY_ARGS)
        self.setFixedSize(p.GEOMETRY_ARGS[2], p.GEOMETRY_ARGS[3])
        self.setWindowTitle(p.TITULO)
        self.setStyleSheet(f'background-color : {p.COLOR_FONDO};')