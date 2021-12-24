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

        # Header
        self.contenedor_titulo = QHBoxLayout()
        self.label_titulo = QLabel(p.STR_HEADER_PRINCIPAL, self)
        # self.label_titulo.setStyleSheet('border : 1px solid black;')
        self.contenedor_titulo.addStretch(1)
        self.contenedor_titulo.addWidget(self.label_titulo)
        self.contenedor_titulo.addStretch(1)

        # Descripción
        self.contenedor_descripcion = QHBoxLayout()
        self.label_descripcion = QLabel(p.STR_DESCRIPCION_PRINCIPAL, self)
        self.label_descripcion.setFixedWidth(500)
        self.label_descripcion.setWordWrap(True)
        self.label_descripcion.setAlignment(Qt.AlignCenter)
        # self.label_descripcion.setStyleSheet('border : 1px solid black;')
        self.contenedor_descripcion.addStretch(1)
        self.contenedor_descripcion.addWidget(self.label_descripcion)
        self.contenedor_descripcion.addStretch(1)

        # Imagen
        self.contenedor_imagen = QHBoxLayout()
        self.label_imagen = QLabel(self)
        self.pixeles_imagen = None
        self.label_imagen.setFixedSize(*p.SIZE_IMAGEN)
        self.label_imagen.setStyleSheet('border : 1px solid black')
        self.contenedor_imagen.addStretch(1)
        self.contenedor_imagen.addWidget(self.label_imagen)
        self.contenedor_imagen.addStretch(1)

        # Botones
        self.contenedor_botones = QHBoxLayout()

        self.boton_guardar = QPushButton('Guardar', self)
        self.boton_siguiente = QPushButton('Siguiente', self)
        self.contenedor_botones.addStretch(1)
        self.contenedor_botones.addWidget(self.boton_guardar)
        self.contenedor_botones.addStretch(1)
        self.contenedor_botones.addWidget(self.boton_siguiente)
        self.contenedor_botones.addStretch(1)

        self.contenedor_volver = QHBoxLayout()
        self.boton_volver = QPushButton('Volver', self)
        self.contenedor_volver.addStretch(1)
        self.contenedor_volver.addWidget(self.boton_volver)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(self.contenedor_titulo)
        vbox.addStretch(1)
        vbox.addLayout(self.contenedor_descripcion)
        vbox.addLayout(self.contenedor_imagen)
        vbox.addStretch(1)
        vbox.addLayout(self.contenedor_botones)
        vbox.addStretch(1)
        vbox.addLayout(self.contenedor_volver)
        self.setLayout(vbox)