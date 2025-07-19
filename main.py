#!/usr/bin/env python3
# main.py
import sys
from PyQt5.QtWidgets import QApplication

from browser.main_window import WebBrowser





def main():
    """Función principal para inicializar y ejecutar la aplicación"""
    app = QApplication(sys.argv)
    app.setApplicationName("Navegador Web Simple")
    app.setApplicationVersion("1.0.0")
    
    # Crear y mostrar navegador
    browser = WebBrowser()
    browser.show()
    
    # Ejecutar aplicación
    sys.exit(app.exec_())





if __name__ == "__main__":
    main()