# Pywkit Browser
Un navegador web simple y funcional desarrollado en Python.

## Características
- Navegación web básica (adelante, atrás, recargar, detener)
- Barra de direcciones con autocompletado de protocolo
- Gestión de perfiles persistente con almacenamiento local
- Interfaz de usuario intuitiva con tooltips
- Manejo de estados de navegación (botones habilitados/deshabilitados)
- Indicador visual de carga de páginas
- Título de ventana dinámico según la página visitada

## Instalación
### 1. Clonar el repositorio
```bash
git clone https://github.com/rodolfocasan/pywkit-browser.git
cd pywkit-browser
```

### 2. Crear entorno virtual (recomendado)
```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En Linux/macOS
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip3 install -r DOCs/requirements.txt
```


## Uso
### Ejecutar el navegador
```bash
python3 main.py
```


## Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request