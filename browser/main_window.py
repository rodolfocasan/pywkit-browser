# browser/main_window.py
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import QUrl

from .profile_manager import BrowserProfileManager
from .navigation_bar import NavigationBar
from .web_view import WebView
from .config import BrowserConfig





class WebBrowser(QMainWindow):
    """ Ventana principal del navegador web con funcionalidades básicas """
    
    def __init__(self):
        super().__init__()
        self.profile_manager = BrowserProfileManager()
        self.setup_window()
        self.setup_ui()
        self.connect_signals()
        self.load_initial_page()
    
    def setup_window(self):
        """ Configurar propiedades básicas de la ventana """
        self.setWindowTitle(BrowserConfig().WINDOW_TITLE)
        self.setGeometry(100, 100, 1200, 800)
    
    def setup_ui(self):
        """ Configurar la interfaz de usuario """
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Crear componentes
        self.navigation_bar = NavigationBar()
        self.web_view = WebView(self.profile_manager.get_profile())
        
        # Añadir componentes al layout
        layout.addWidget(self.navigation_bar)
        layout.addWidget(self.web_view)
    
    def connect_signals(self):
        """ Conectar señales entre componentes """
        # Señales de la barra de navegación
        self.navigation_bar.navigate_requested.connect(self.web_view.navigate_to_url)
        self.navigation_bar.back_requested.connect(self.web_view.back)
        self.navigation_bar.forward_requested.connect(self.web_view.forward)
        self.navigation_bar.reload_requested.connect(self._handle_reload_request)
        
        # Señales de la vista web
        self.web_view.urlChanged.connect(self.navigation_bar.update_url)
        self.web_view.navigation_state_changed.connect(
            self.navigation_bar.update_navigation_buttons
        )
        self.web_view.loading_state_changed.connect(
            self.navigation_bar.set_loading_state
        )
        
        # Señal para actualizar título de ventana
        self.web_view.titleChanged.connect(self._update_window_title)
    
    def _handle_reload_request(self):
        """ Manejar solicitud de recarga/detención """
        if self.navigation_bar.reload_btn.text() == "✕":
            self.web_view.stop()
        else:
            self.web_view.reload()
    
    def _update_window_title(self, title):
        """ Actualizar título de la ventana """
        if title:
            self.setWindowTitle(f"{title} - {BrowserConfig().WINDOW_TITLE}")
        else:
            self.setWindowTitle(BrowserConfig().WINDOW_TITLE)
    
    def load_initial_page(self):
        """ Cargar página inicial """
        initial_url = QUrl("https://www.google.com")
        self.web_view.navigate_to_url(initial_url)
    
    def closeEvent(self, event):
        """ Manejar cierre de la aplicación """
        event.accept()