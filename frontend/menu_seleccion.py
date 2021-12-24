from PyQt5.QtCore import QLine, pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QFont, QPixelFormat, QPixmap
from PyQt5.QtWidgets import (QApplication, QComboBox, QMainWindow, QWidget)
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
        self.setFixedSize(p.GEOMETRY_ARGS[2], p.GEOMETRY_ARGS[3])
        self.setWindowTitle(p.TITULO)
        self.setStyleSheet(f'background-color : {p.COLOR_FONDO};')

        # Header
        self.contenedor_titulo = QHBoxLayout()
        self.label_titulo = QLabel(p.STR_HEADER_SELECCION, self)
        # self.label_titulo.setStyleSheet('border : 1px solid black;')
        self.contenedor_titulo.addStretch(1)
        self.contenedor_titulo.addWidget(self.label_titulo)
        self.contenedor_titulo.addStretch(1)

        # Descripción
        self.contenedor_descripcion = QHBoxLayout()
        self.label_descripcion = QLabel(p.STR_DESCRIPCION_SELECCION, self)
        self.label_descripcion.setFixedWidth(500)
        self.label_descripcion.setWordWrap(True)
        self.label_descripcion.setAlignment(Qt.AlignLeft)
        # self.label_descripcion.setStyleSheet('border : 1px solid black;')
        self.contenedor_descripcion.addStretch(1)
        self.contenedor_descripcion.addWidget(self.label_descripcion)
        self.contenedor_descripcion.addStretch(1)

        # Listas desplegables
        self.contenedor_listas = QHBoxLayout()
        
        # - Elección de tipo
        self.selector_tipo = QComboBox(self)
        self.selector_tipo.setMinimumSize(80, 30)
        self.selector_tipo.adjustSize()
        self.selector_tipo.addItems(p.TIPOS)
        font = QFont('Arial', 12)
        self.selector_tipo.setFont(font)
        
        # - Elección de categoría
        self.selector_categoria = QComboBox(self)
        self.selector_categoria.setMinimumSize(80, 30)
        self.selector_categoria.adjustSize()
        self.selector_categoria.addItems(p.CATEGORIAS)
        font = QFont('Arial', 12)
        self.selector_categoria.setFont(font)

        self.contenedor_listas.addStretch(1)
        self.contenedor_listas.addWidget(self.selector_tipo)
        self.contenedor_listas.addStretch(1)
        self.contenedor_listas.addWidget(self.selector_categoria)
        self.contenedor_listas.addStretch(1)

        # Botón
        self.contenedor_boton = QHBoxLayout()
        self.boton = QPushButton('Generar imagen', self)
        self.contenedor_boton.addStretch(1)
        self.contenedor_boton.addWidget(self.boton)
        self.contenedor_boton.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(self.contenedor_titulo)
        vbox.addStretch(2)
        vbox.addLayout(self.contenedor_descripcion)
        vbox.addStretch(1)
        vbox.addLayout(self.contenedor_listas)
        vbox.addStretch(1)
        vbox.addLayout(self.contenedor_boton)
        vbox.addStretch(2)
        self.setLayout(vbox)