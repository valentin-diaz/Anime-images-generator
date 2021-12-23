import sys
from PyQt5.QtWidgets import QApplication

from frontend.menu_inicial import MenuInicial
from frontend.menu_seleccion import MenuSeleccion

if __name__ == '__main__':
    app = QApplication([])

    # Instancias de frontend
    menu_inicial = MenuInicial()
    menu_seleccion = MenuSeleccion()

    # Conexión de señales
    menu_inicial.senal_ir_a_seleccion.connect(menu_seleccion.show)
    menu_inicial.senal_ir_a_seleccion.connect(menu_inicial.close)


    # Iniciar el flujo del programa
    menu_inicial.show()

    sys.exit(app.exec_())