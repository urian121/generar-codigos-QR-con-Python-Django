from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse, Http404
import qrcode  # Importamos el modulo necesario para trabajar con codigos QR de Python
import uuid  # Modulo de python para crear un string
import os  # Modulo para obtener la ruta o directorio


def index(request):
    return render(request, 'index.html')


def generar_qr(request):
    if request.method == 'POST':
        # Recibiendo string desde el form para convertir a QR
        texto = request.POST['texto']
        
        # Codificando datos usando la función make()
        img = qrcode.make(texto)
        
        # Nombre aleatorio para el QR
        nombreQR = uuid.uuid4().hex + '.png'
        
        # Path para guardar el codigo qr en media
        basepath = os.path.join(settings.MEDIA_ROOT, 'qrs')
        
        # Crear la carpeta si no existe
        os.makedirs(basepath, exist_ok=True)
        
        # Guardar como un archivo de imagen
        img.save(os.path.join(basepath, nombreQR))
        
        # Ruta media para la imagen
        ruta_imagen = f'{settings.MEDIA_URL}qrs/{nombreQR}'
        
        return render(request, 'index.html', {
            'imgQR': nombreQR,
            'ruta_imagen': ruta_imagen
        })
    return render(request, 'index.html')


def descargar_qr(request, nombreImagenQR):
    """Función para descargar el código QR generado"""
    basepath = os.path.join(settings.MEDIA_ROOT, 'qrs')
    url_file = os.path.join(basepath, nombreImagenQR)
    
    if os.path.exists(url_file):
        return FileResponse(
            open(url_file, 'rb'),
            as_attachment=True,
            filename=nombreImagenQR
        )
    raise Http404("El archivo QR no existe")