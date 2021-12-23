from PyQt5.QtCore import QLine, pyqtSignal
from PyQt5.QtGui import QIcon, QFont, QPixelFormat, QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget)
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout)
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, QAction)

import parametros as p

class MenuInicial(QWidget):
    '''
    Muestra una pequeña descripción de la aplicación y permite pasar al menú de selección
    '''

    def __init__(self) -> None:
        super().__init__()
        self.init_gui()

    def init_gui(self):
        # Configuración inicial de la ventana
        self.setGeometry(*p.GEOMETRY_ARGS)
        self.setWindowTitle(p.TITULO)

        