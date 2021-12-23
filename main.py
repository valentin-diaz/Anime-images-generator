import sys
from PyQt5.QtWidgets import QApplication

from frontend.menu_inicial import MenuInicial

if __name__ == '__main__':
    app = QApplication([])

    menu_inicial = MenuInicial()
    menu_inicial.show()

    sys.exit(app.exec_())