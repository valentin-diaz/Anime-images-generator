from PyQt5.QtCore import QLine, pyqtSignal, Qt
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
        self.setStyleSheet(f'background-color : {p.COLOR_FONDO};')

        # Header
        self.contenedor_titulo = QHBoxLayout()
        self.label_titulo = QLabel(p.STR_HEADER_INICIO, self)
        # self.label_titulo.setStyleSheet('border : 1px solid black;')
        self.contenedor_titulo.addStretch(1)
        self.contenedor_titulo.addWidget(self.label_titulo)
        self.contenedor_titulo.addStretch(1)

        # Descripción
        self.contenedor_descripcion = QHBoxLayout()
        self.label_descripcion = QLabel(p.STR_DESCRIPCION_INICIO, self)
        self.label_descripcion.setFixedWidth(500)
        self.label_descripcion.setWordWrap(True)
        self.label_descripcion.setAlignment(Qt.AlignCenter)
        self.label_descripcion.openExternalLinks()
        # self.label_descripcion.setStyleSheet('border : 1px solid black;')
        self.contenedor_descripcion.addStretch(1)
        self.contenedor_descripcion.addWidget(self.label_descripcion)
        self.contenedor_descripcion.addStretch(1)

        # Botón
        self.contenedor_boton = QHBoxLayout()
        self.boton = QPushButton('Iniciar', self)
        self.contenedor_boton.addStretch(1)
        self.contenedor_boton.addWidget(self.boton)
        self.contenedor_boton.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addLayout(self.contenedor_titulo)
        vbox.addStretch(1)
        vbox.addLayout(self.contenedor_descripcion)
        vbox.addStretch(1)
        vbox.addLayout(self.contenedor_boton)
        vbox.addStretch(2)
        self.setLayout(vbox)
