from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generar_qr/', views.generar_qr, name='generar_qr'),
    path('descargar-qr/<str:nombreImagenQR>/', views.descargar_qr, name='descargar_qr'),
]