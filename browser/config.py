# browser/config.py
import os





class BrowserConfig:
    """ Configuraciones generales del navegador """
    
    # Configuraciones de ventana
    WINDOW_TITLE = "Pywkit Browser"
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800
    WINDOW_X = 100
    WINDOW_Y = 100
    
    # Configuraciones de perfil
    PROFILE_NAME = "Pywkit"
    DATA_DIRECTORY = os.path.join(os.getcwd(), "browser_data")
    
    # URL inicial
    INITIAL_URL = "https://www.google.com"
    
    # Configuraciones de interfaz
    NAVIGATION_BUTTONS = {
        'back': "←",
        'forward': "→",
        'reload': "⟳",
        'stop': "✕"
    }
    
    # Tooltips
    TOOLTIPS = {
        'back': "Atrás",
        'forward': "Adelante",
        'reload': "Recargar",
        'stop': "Detener"
    }
    
    # Placeholders
    URL_PLACEHOLDER = "Ingresa una URL..."
    
    @classmethod
    def get_data_directory(cls):
        """ Obtener directorio de datos, creándolo si no existe """
        if not os.path.exists(cls.DATA_DIRECTORY):
            os.makedirs(cls.DATA_DIRECTORY)
        return cls.DATA_DIRECTORY
    
    @classmethod
    def get_cache_directory(cls):
        """ Obtener directorio de caché """
        return os.path.join(cls.get_data_directory(), "cache")