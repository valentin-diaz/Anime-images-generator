import sys
from PyQt5.QtWidgets import QApplication

from frontend.menu_inicial import MenuInicial
from frontend.menu_seleccion import MenuSeleccion
from frontend.menu_principal import MenuPrincipal

from backend.logica_principal import LogicaPrincipal

if __name__ == '__main__':
    app = QApplication([])

    # Instancias de frontend
    menu_inicial = MenuInicial()
    menu_seleccion = MenuSeleccion()
    menu_principal = MenuPrincipal()

    # Instancias de backend
    logica_principal = LogicaPrincipal()

    # Conexión de señales
    menu_inicial.senal_ir_a_seleccion.connect(menu_seleccion.show)
    menu_inicial.senal_ir_a_seleccion.connect(menu_inicial.close)

    menu_seleccion.senal_ir_a_principal.connect(logica_principal.iniciar_menu)
    logica_principal.senal_mostrar_menu.connect(menu_principal.show)
    logica_principal.senal_mostrar_menu.connect(menu_seleccion.hide)

    logica_principal.senal_enviar_jpg.connect(menu_principal.recibir_jpg)
    logica_principal.senal_enviar_gif.connect(menu_principal.recibir_gif)

    menu_principal.senal_cambiar_imagen.connect(logica_principal.siguiente_imagen)

    menu_principal.senal_volver.connect(logica_principal.resetear_atributos)
    menu_principal.senal_volver.connect(menu_seleccion.show)
    menu_principal.senal_volver.connect(menu_principal.hide)

    menu_principal.senal_guardar_imagen.connect(logica_principal.guardar_imagen)


    # Iniciar el flujo del programa
    menu_inicial.show()

    sys.exit(app.exec_())