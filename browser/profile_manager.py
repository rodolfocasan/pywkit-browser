# browser/profile_manager.py
import os
from PyQt5.QtWebEngineWidgets import QWebEngineProfile

from .config import BrowserConfig





class BrowserProfileManager:
    """ Gestiona la configuración y almacenamiento del perfil del navegador """
    def __init__(self, profile_name=BrowserConfig().PROFILE_NAME):
        self.profile_name = profile_name
        self.browser_data_dir = None
        self.profile = None
        self.setup_profile()
    
    def setup_profile(self):
        """ Configurar el perfil del navegador con directorio personalizado """
        # Crear directorio para datos del navegador
        self.browser_data_dir = os.path.join(os.getcwd(), "browser_data")
        if not os.path.exists(self.browser_data_dir):
            os.makedirs(self.browser_data_dir)
        
        # Crear perfil personalizado
        self.profile = QWebEngineProfile(self.profile_name)
        self.profile.setPersistentStoragePath(self.browser_data_dir)
        self.profile.setCachePath(os.path.join(self.browser_data_dir, "cache"))
        print(f" - Datos del navegador se almacenarán en: {self.browser_data_dir}")
    
    def get_profile(self):
        """ Obtener el perfil configurado """
        return self.profile
    
    def get_data_directory(self):
        """ Obtener el directorio de datos """
        return self.browser_data_dir
    
    def clear_cache(self):
        """ Limpiar caché del navegador """
        if self.profile:
            # Aquí podrías implementar limpieza personalizada
            pass