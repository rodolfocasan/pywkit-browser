# browser/web_view.py
from PyQt5.QtCore import pyqtSignal, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage





class WebView(QWebEngineView):
    """ Vista web personalizada con funcionalidades extendidas """
    
    # Señales personalizadas
    navigation_state_changed = pyqtSignal(bool, bool)  # can_go_back, can_go_forward
    loading_state_changed = pyqtSignal(bool)  # is_loading
    
    def __init__(self, profile, parent=None):
        super().__init__(parent)
        self.setup_page(profile)
        self.connect_signals()
    
    def setup_page(self, profile):
        """ Configurar la página web con el perfil dado """
        page = QWebEnginePage(profile, self)
        self.setPage(page)
    
    def connect_signals(self):
        """ Conectar señales internas """
        self.loadFinished.connect(self._on_load_finished)
        self.loadStarted.connect(self._on_load_started)
        self.urlChanged.connect(self._on_url_changed)
    
    def _on_load_finished(self, success):
        """ Manejar finalización de carga """
        self.loading_state_changed.emit(False)
        self._emit_navigation_state()
    
    def _on_load_started(self):
        """ Manejar inicio de carga """
        self.loading_state_changed.emit(True)
    
    def _on_url_changed(self, url):
        """ Manejar cambio de URL """
        self._emit_navigation_state()
    
    def _emit_navigation_state(self):
        """ Emitir estado actual de navegación """
        history = self.history()
        can_go_back = history.canGoBack()
        can_go_forward = history.canGoForward()
        self.navigation_state_changed.emit(can_go_back, can_go_forward)
    
    def navigate_to_url(self, url):
        """ Navegar a una URL específica """
        if isinstance(url, str):
            url = QUrl(url)
        self.setUrl(url)
    
    def get_current_url(self):
        """ Obtener la URL actual """
        return self.url()
    
    def get_page_title(self):
        """ Obtener el título de la página actual """
        return self.title()