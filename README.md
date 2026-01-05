# Generador de Códigos QR con Python + Django

Sistema web simple para generar códigos QR a partir de texto. Permite crear códigos QR dinámicamente y descargarlos como imágenes PNG.


![Resultado](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/refs/heads/master/generar-codigos-QR-con-python-django.png)


## ¿Qué hace este proyecto?

- Convierte cualquier texto en un código QR
- Genera imágenes QR únicas con nombres aleatorios
- Permite visualizar y descargar los códigos QR generados
- Interfaz web simple y fácil de usar

## Requisitos

- Python 3.x
- Django 5.2.9
- qrcode 8.2
- pillow 12.1.0

## Instalación y Ejecución

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Ejecutar el servidor

```bash
python manage.py runserver
```

### 3. Abrir en el navegador

Abre tu navegador y ve a: `http://127.0.0.1:8000/`

## Uso

1. Ingresa el texto que deseas convertir a QR en el formulario
2. Haz clic en "Generar QR"
3. El código QR se mostrará en pantalla
4. Puedes descargarlo haciendo clic en "Descargar QR"

## Estructura del Proyecto

- `generador_qr/` - Aplicación principal
  - `views.py` - Lógica para generar y descargar QR
  - `templates/` - Plantillas HTML
  - `urls.py` - Rutas de la aplicación
- `media/qrs/` - Carpeta donde se guardan los códigos QR generados
- `project_core/` - Configuración principal de Django

## Tecnologías Utilizadas

- **Django** - Framework web
- **qrcode** - Generación de códigos QR
- **Pillow** - Procesamiento de imágenes
- **Bootstrap 5** - Estilos y diseño responsive
