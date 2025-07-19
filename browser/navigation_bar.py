# browser/navigation_bar.py
from PyQt5.QtCore import pyqtSignal, QUrl
from PyQt5.QtWidgets import QToolBar, QPushButton, QLineEdit





class NavigationBar(QToolBar):
    """ Barra de navegación con controles de navegación y barra de direcciones """
    
    # Señales personalizadas
    navigate_requested = pyqtSignal(QUrl)
    back_requested = pyqtSignal()
    forward_requested = pyqtSignal()
    reload_requested = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMovable(False)
        self.setup_ui()
        self.connect_signals()
    
    def setup_ui(self):
        """ Configurar la interfaz de la barra de navegación """
        # Botón atrás
        self.back_btn = QPushButton("←")
        self.back_btn.setToolTip("Atrás")
        self.back_btn.setEnabled(False)
        self.addWidget(self.back_btn)
        
        # Botón adelante
        self.forward_btn = QPushButton("→")
        self.forward_btn.setToolTip("Adelante")
        self.forward_btn.setEnabled(False)
        self.addWidget(self.forward_btn)
        
        # Botón recargar
        self.reload_btn = QPushButton("⟳")
        self.reload_btn.setToolTip("Recargar")
        self.addWidget(self.reload_btn)
        
        # Barra de direcciones
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Ingresa una URL...")
        self.addWidget(self.url_bar)
    
    def connect_signals(self):
        """ Conectar señales internas """
        self.back_btn.clicked.connect(self.back_requested.emit)
        self.forward_btn.clicked.connect(self.forward_requested.emit)
        self.reload_btn.clicked.connect(self.reload_requested.emit)
        self.url_bar.returnPressed.connect(self._handle_url_input)
    
    def _handle_url_input(self):
        """ Manejar entrada de URL en la barra de direcciones """
        url_text = self.url_bar.text().strip()
        if not url_text:
            return
        
        # Añadir protocolo si no lo tiene
        if not url_text.startswith(('http://', 'https://')):
            url_text = f"https://{url_text}"
        
        url = QUrl(url_text)
        self.navigate_requested.emit(url)
    
    def update_url(self, url):
        """ Actualizar la URL mostrada en la barra de direcciones """
        self.url_bar.setText(url.toString())
    
    def update_navigation_buttons(self, can_go_back, can_go_forward):
        """ Actualizar el estado de los botones de navegación """
        self.back_btn.setEnabled(can_go_back)
        self.forward_btn.setEnabled(can_go_forward)
    
    def set_loading_state(self, is_loading):
        """ Actualizar interfaz según estado de carga """
        if is_loading:
            self.reload_btn.setText("✕")
            self.reload_btn.setToolTip("Detener")
        else:
            self.reload_btn.setText("⟳")
            self.reload_btn.setToolTip("Recargar")