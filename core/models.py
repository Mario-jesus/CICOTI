from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class SiteConfiguration(models.Model):

    site_name = models.CharField(max_length=20, verbose_name="Nombre del sitio")
    site_logo = models.ImageField(upload_to="core", verbose_name="Logo del sitio")
    navbar_logo = models.ImageField(upload_to="core", verbose_name="Logo de la barra de navegación")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Configuración del sitio"
        verbose_name_plural = "Configuración del sitio"

    def __str__(self) -> str:
        return self.site_name


class Modal(models.Model):

    header_image = models.ImageField(upload_to="core", verbose_name="Imagen del encabezado")
    footer_image = models.ImageField(upload_to="core", verbose_name="Imagen del pie")
    left_title = models.CharField(max_length=40, verbose_name="Título izquierdo")
    left_description = models.CharField(max_length=40, verbose_name="Descripción izquierda")
    left_cta = models.URLField(verbose_name="Enlace del boton izquierdo")
    right_title = models.CharField(max_length=40, verbose_name="Título derecho")
    right_description = models.CharField(max_length=40, verbose_name="Descripción derecha")
    right_cta = models.URLField(verbose_name="Enlace del boton derecho")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Modal"
        verbose_name_plural = "Modal"

    def __str__(self) -> str:
        return "Modal"


class Footer(models.Model):

    address = models.CharField(max_length=120, verbose_name="Dirección")
    phone = models.CharField(max_length=25, verbose_name="Teléfono")
    link_CA = models.URLField(verbose_name="Web de Computo Distribuido")
    email = models.EmailField(verbose_name="Correo")
    social_facebook = models.URLField(verbose_name="Facebook")
    social_youtube = models.URLField(verbose_name="Youtube")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footer"

    def __str__(self) -> str:
        return "Footer"



class Home(models.Model):

    hero_title = models.CharField(max_length=100, verbose_name="Título (portada)")
    hero_date = models.CharField(max_length=50, verbose_name="Fecha (portada)")
    hero_place = models.CharField(max_length=100, verbose_name="Lugar (portada)")
    start_date = models.DateTimeField(verbose_name="Fecha de inicio del evento")
    body_title = models.CharField(max_length=100, verbose_name="Título")
    body_date = models.CharField(max_length=50, verbose_name="Fecha")
    body_modality = models.CharField(max_length=30, verbose_name="Modalidad")
    body_content = RichTextField(verbose_name="Contenido del cuerpo")
    aside_title = models.CharField(max_length=80, verbose_name="Título de la barra lateral")
    aside_content = RichTextField(verbose_name="Contenido de la barra lateral")
    cta = models.URLField(verbose_name="Enlace del programa")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Inicio"
        verbose_name_plural = "Inicio"

    def __str__(self) -> str:
        return "Inicio"
